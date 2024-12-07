<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preprocessing Data</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      background-color: #f4f4f9;
    }
    h1 {
      text-align: center;
    }
    .container {
      max-width: 900px;
      margin: 0 auto;
      padding: 20px;
      background: white;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      border-radius: 8px;
    }
    .upload-btn {
      display: block;
      margin: 20px auto;
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      font-size: 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .upload-btn:hover {
      background-color: #0056b3;
    }
    .table-container {
      margin-top: 20px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    table, th, td {
      border: 1px solid #ddd;
    }
    th, td {
      padding: 10px;
      text-align: left;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>Preprocessing Data: PKPA and BAAK</h1>
    
    <!-- Upload buttons for both datasets -->
    <input type="file" id="upload-pkpa" class="upload-btn" accept=".xlsx,.xls,.csv" />
    <input type="file" id="upload-baak" class="upload-btn" accept=".xlsx,.xls,.csv" />

    <div id="error-message"></div>

    <!-- Display processed table -->
    <div class="table-container">
      <h2>Processed Data (Filtered and Joined)</h2>
      <table id="data-table"></table>
    </div>
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.17.4/xlsx.full.min.js"></script>

  <script>
    let processedDataPkpa = [];
    let processedDataBaak = [];

    // Function to read and process PKPA dataset
    document.getElementById('upload-pkpa').addEventListener('change', function (e) {
      let file = e.target.files[0];
      if (file) {
        let reader = new FileReader();
        reader.onload = function(event) {
          let data = new Uint8Array(event.target.result);
          let workbook = XLSX.read(data, {type: 'array'});
          
          let sheet = workbook.Sheets["Rekap"];
          if (sheet) {
            let json = XLSX.utils.sheet_to_json(sheet, {header: 1});
            let processedData = json.slice(1).map(row => ({
              "Kode Progdi": row[2], "nim": row[3], "nama": row[4], "pekerjaan": row[19], "ketereratan": row[28]
            })).filter(row => row["nim"].toString().length === 9 && !["01", "02", "03"].includes(row["Kode Progdi"]));
            processedDataPkpa = processedData;
            console.log("PKPA Data Processed: ", processedDataPkpa);
          } else {
            alert("Sheet 'Rekap' tidak ditemukan di file PKPA.");
          }
        };
        reader.readAsArrayBuffer(file);
      }
    });

    // Function to read and process BAAK dataset
    document.getElementById('upload-baak').addEventListener('change', function (e) {
      let file = e.target.files[0];
      if (file) {
        let reader = new FileReader();
        reader.onload = function(event) {
          let data = new Uint8Array(event.target.result);
          let workbook = XLSX.read(data, {type: 'array'});
          
          let sheets = workbook.Sheets;
          for (let sheetName in sheets) {
            let sheet = sheets[sheetName];
            let json = XLSX.utils.sheet_to_json(sheet, {header: 1});
            let processedData = json.slice(1).map(row => ({
              "nim": row[1], "nama": row[2], "ipk": row[4], "lama studi": row[5]
            })).filter(row => !["01", "02", "03"].includes(row["nim"].substring(4,6)));
            processedDataBaak.push(...processedData);
          }
          console.log("BAAK Data Processed: ", processedDataBaak);
        };
        reader.readAsArrayBuffer(file);
      }
    });

    // Function to combine and join datasets
    function joinAndDisplayData() {
      if (processedDataPkpa.length > 0 && processedDataBaak.length > 0) {
        let pkpaDf = processedDataPkpa;
        let baakDf = processedDataBaak;

        // Merge on 'nim' column
        let joinedData = pkpaDf.filter(pkpaRow => baakDf.some(baakRow => baakRow.nim === pkpaRow.nim))
          .map(pkpaRow => {
            let baakRow = baakDf.find(row => row.nim === pkpaRow.nim);
            return {
              "ipk": baakRow.ipk,
              "lama studi": baakRow["lama studi"],
              "ketereratan": pkpaRow.ketereratan
            };
          })
          .filter(row => row.ketereratan !== "0");

        // Display data in table
        const table = document.getElementById('data-table');
        table.innerHTML = "<tr><th>IPK</th><th>Lama Studi</th><th>Ketereratan</th></tr>"; // Table headers
        joinedData.forEach(row => {
          let rowHtml = `<tr><td>${row.ipk}</td><td>${row["lama studi"]}</td><td>${row.ketereratan}</td></tr>`;
          table.innerHTML += rowHtml;
        });
      } else {
        alert("Data tidak cukup untuk dilakukan join.");
      }
    }

    // After both datasets are uploaded and processed, join the data
    function checkAndJoin() {
      if (processedDataPkpa.length > 0 && processedDataBaak.length > 0) {
        joinAndDisplayData();
      }
    }

    // Monitor when both datasets are processed
    setInterval(checkAndJoin, 2000);  // Check every 2 seconds for both datasets

  </script>

</body>
</html>
