const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");
const lineWidth = document.getElementById("line-width");
const cleanBtn = document.getElementById("clean-btn");
const eraserBtn = document.getElementById("eraser-btn");
const guessBtn = document.getElementById("guess-btn");

const CANVAS_WIDTH = 400;
const CANVAS_HEIGHT = 400;
let isPainting = false;
let isErase = true;

canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;
ctx.lineWidth = lineWidth.value;

function onMove(event){
    if (isPainting){
        ctx.lineTo(event.offsetX, event.offsetY);
        ctx.stroke();
        return;
    }
    ctx.moveTo(event.offsetX, event.offsetY);
}

function startPainting(){
    isPainting = true;
}

function cancelPainting(){
    isPainting = false;
    ctx.beginPath();
}

function onLineWidthChange(event){
    ctx.lineWidth = event.target.value;
}

function onCleanClick(){
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
}

function onEraserClick(){
    if (isErase) {
        ctx.strokeStyle = "white";
        eraserBtn.innerText = "Draw";
        isErase = false;
    } else {
        ctx.strokeStyle = "black";
        eraserBtn.innerText = "Erase";
        isErase = true;
    }
}

function onGuessClick(){
    const url = canvas.toDataURL('image/png');
    console.log(url);
    document.getElementById("guess-input").value = url;
}


canvas.addEventListener("mousemove", onMove);
canvas.addEventListener("mousedown", startPainting);
canvas.addEventListener("mouseup", cancelPainting);
canvas.addEventListener("mouseleave", cancelPainting);

lineWidth.addEventListener("change", onLineWidthChange);
cleanBtn.addEventListener("click", onCleanClick);
eraserBtn.addEventListener("click", onEraserClick);
guessBtn.addEventListener("click", onGuessClick);