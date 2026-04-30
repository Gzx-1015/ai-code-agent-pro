async function analyze() {
    const code = document.getElementById("code").value;

    const res = await fetch("http://127.0.0.1:8000/review", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({code})
    });

    const data = await res.json();
    document.getElementById("output").innerText =
        "Review:\n" + data.review +
        "\n\nSecurity:\n" + data.security +
        "\n\nPatch:\n" + data.patch;
}
