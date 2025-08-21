function sendCommand() {
    const command = document.getElementById("commandInput").value;
    
    fetch("/command", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ command: command })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = "AssistantAI: " + data.response;
    });
}
