pip install xlrd
pip install openpyxl
import streamlit as st
import pandas as pd

# Fungsi untuk memproses data dari PKPA
def process_sheet_rekap(file):
    try:
        # Menentukan engine berdasarkan ekstensi file
        engine = "xlrd" if file.name.endswith(".xls") else "openpyxl"

        # Membaca sheet bernama "Rekap"
        excel_file = pd.ExcelFile(file, engine=engine)
        if "Rekap" in excel_file.sheet_names:
            df = pd.read_excel(file, sheet_name="Rekap", usecols="C,D,E,T,AC", skiprows=1, engine=engine)
            df.columns = ["Kode Progdi", "nim", "nama", "pekerjaan", "ketereratan"]
            df = df.dropna()  # Menghapus baris dengan missing values
            df = df[~df['Kode Progdi'].isin(['01', '02', '03'])]  # Menghapus kode tertentu
            df = df[df['nim'].apply(lambda x: len(str(x)) == 9)]  # Validasi panjang 'nim'
            return df
        else:
            st.warning("Sheet 'Rekap' tidak ditemukan dalam file.")
            return None
    except Exception as e:
        st.error(f"Error saat memproses file PKPA: {e}")
        return None

# Fungsi untuk memproses data dari BAAK
def process_all_sheets_baak(file):
    try:
        # Menentukan engine berdasarkan ekstensi file
        engine = "xlrd" if file.name.endswith(".xls") else "openpyxl"

        # Membaca semua sheet
        excel_file = pd.ExcelFile(file, engine=engine)
        processed_sheets = []
        for sheet in excel_file.sheet_names:
            df = pd.read_excel(file, sheet_name=sheet, usecols="B,C,E,F", skiprows=1, engine=engine)
            df.columns = ["nim", "nama", "ipk", "lama studi"]
            df = df.dropna()  # Menghapus missing values
            df = df[~df['nim'].apply(lambda x: str(x)[4:6] in ['01', '02', '03'])]  # Validasi 'nim'
            processed_sheets.append(df)
        if processed_sheets:
            return pd.concat(processed_sheets, ignore_index=True)
        else:
            return None
    except Exception as e:
        st.error(f"Error saat memproses file BAAK: {e}")
        return None

# Fungsi untuk melakukan join data
def join_data(df_pkpa, df_baak):
    try:
        joined_df = pd.merge(df_pkpa, df_baak, on="nim", how="inner")
        filtered_df = joined_df[["ipk", "lama studi", "ketereratan"]]  # Kolom yang diambil
        filtered_df = filtered_df[filtered_df["ketereratan"] != 0]  # Filter ketereratan = 0
        return filtered_df
    except Exception as e:
        st.error(f"Error saat melakukan join data: {e}")
        return None

# Streamlit Web Interface
st.title("Aplikasi Preprocessing Data")
st.write("Unggah file PKPA dan BAAK untuk melakukan preprocessing data.")

# Unggah file PKPA
uploaded_pkpa = st.file_uploader("Unggah File PKPA", type=["xlsx", "xls"])
if uploaded_pkpa:
    df_pkpa = process_sheet_rekap(uploaded_pkpa)
    if df_pkpa is not None:
        st.success("Data PKPA berhasil diproses!")
        st.dataframe(df_pkpa)

# Unggah file BAAK
uploaded_baak = st.file_uploader("Unggah File BAAK", type=["xlsx", "xls"])
if uploaded_baak:
    df_baak = process_all_sheets_baak(uploaded_baak)
    if df_baak is not None:
        st.success("Data BAAK berhasil diproses!")
        st.dataframe(df_baak)

# Lakukan Join Data
if uploaded_pkpa and uploaded_baak:
    st.write("**Hasil Join Data:**")
    joined_data = join_data(df_pkpa, df_baak)
    if joined_data is not None:
        st.success("Data berhasil digabung!")
        st.dataframe(joined_data)

        # Unduh hasil gabungan
        st.download_button(
            label="Unduh Data CSV",
            data=joined_data.to_csv(index=False).encode('utf-8'),
            file_name="joined_data.csv",
            mime="text/csv"
        )
        st.download_button(
            label="Unduh Data Excel",
            data=joined_data.to_excel(index=False, engine='openpyxl'),
            file_name="joined_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
