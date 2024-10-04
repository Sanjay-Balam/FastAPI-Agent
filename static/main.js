document.getElementById("uploadBtn").addEventListener("click", async () => {
    const input = document.getElementById("csvFileInput");
    if (!input.files.length) {
        alert("Please select a CSV file first!");
        return;
    }

    const formData = new FormData();
    formData.append("file", input.files[0]);

    const response = await fetch("http://127.0.0.1:8000/uploadcsv/", {
        method: "POST",
        body: formData
    });

    const result = await response.json();

    // Display JSON data on the page
    document.getElementById("output").innerText = `Extracted JSON: ${JSON.stringify(result.data, null, 2)}`;
});
