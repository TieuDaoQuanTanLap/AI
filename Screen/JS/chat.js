const tinnhan = document.getElementById("tinnhan")
const khungchat = document.getElementById("khungchat")
const gui = document.getElementById("gui")
gui.addEventListener("click", function() {
    sendMessage()
})
khungchat.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        if (khungchat.value == ""){
            alert("Không nhận được tin nhắn!")
        }else {
            sendMessage()
        }
    }
})
function sendMessage() {
    const messenger = khungchat.value
    displayMessage(messenger)
    tinnhan.scrollTop = tinnhan.scrollHeight
}
function displayMessage(message) {
    const hientinnhan = document.createElement("div")
    hientinnhan.classList.add("messenger")
    hientinnhan.innerHTML = message

    tinnhan.appendChild(hientinnhan)
}