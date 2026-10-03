const imageInput = document.getElementById("imageInput");
const chooseBtn = document.getElementById("chooseBtn");
const detectBtn = document.getElementById("detectBtn");
const clearBtn = document.getElementById("clearBtn");
const againBtn = document.getElementById("againBtn");

const preview = document.getElementById("preview");
const fileName = document.getElementById("fileName");

const result = document.getElementById("result");
const prediction = document.getElementById("prediction");

const aiBar = document.getElementById("aiBar");
const humanBar = document.getElementById("humanBar");

const aiPercent = document.getElementById("aiPercent");
const humanPercent = document.getElementById("humanPercent");

const message = document.getElementById("message");

const confidenceBar =
    document.getElementById("confidenceBar");

const confidencePercent =
    document.getElementById("confidencePercent");


// Choose artwork button

chooseBtn.addEventListener("click", function () {

    imageInput.click();

});


// When image is selected

imageInput.addEventListener("change", function () {

    const file = imageInput.files[0];

    if (!file) {
        return;
    }

    fileName.textContent = file.name;

    const imageURL = URL.createObjectURL(file);

    preview.src = imageURL;

    preview.style.display = "inline-block";

    detectBtn.disabled = false;

    result.style.display = "none";

});


// Detect artwork

detectBtn.addEventListener("click", async function () {

    if (!imageInput.files[0]) {
        return;
    }

    result.style.display = "block";

    prediction.innerHTML =
    '<span class="loading">🔍</span> Analyzing artwork...';

await new Promise(resolve => setTimeout(resolve, 2000));

    message.textContent =
        "My tiny art detective is thinking... 🐱✨";


    const formData = new FormData();

    formData.append(
        "image",
        imageInput.files[0]
    );


    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",
                body: formData
            }
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.error || "Prediction failed"
            );

        }


        const ai = data.ai_probability;

        const human = data.human_probability;

        let confidence = Math.max(ai, human);

        confidencePercent.textContent =
            confidence.toFixed(2) + "%";

        confidenceBar.style.width =
            confidence + "%";

let confidenceMessage = "";

if (confidence >= 90) {
    confidenceMessage = "🌟 Very high confidence";
} else if (confidence >= 75) {
    confidenceMessage = "✨ High confidence";
} else if (confidence >= 60) {
    confidenceMessage = "🌸 Moderate confidence";
} else {
    confidenceMessage = "☁️ Low confidence";
}


        aiPercent.textContent =
            ai.toFixed(2) + "%";

        humanPercent.textContent =
            human.toFixed(2) + "%";


        aiBar.style.width =
            ai + "%";

        humanBar.style.width =
            human + "%";


        if (data.prediction === "ai") {

            prediction.textContent =
                "🤖 Likely AI-generated";

            message.textContent =
    "✨ The artwork looks more like AI-generated art! " + confidenceMessage;

        } else {

            prediction.textContent =
                "🎨 Likely Human-created";

            message.textContent =
    "✨ The artwork looks more like human-created art! " + confidenceMessage;

        }


    } catch (error) {

        console.error(error);

        prediction.textContent =
            "😿 Something went wrong";

        message.textContent =
            "Please make sure the Python server is running.";

    }

});


// Clear button

clearBtn.addEventListener("click", function () {

    imageInput.value = "";

    preview.src = "";

    preview.style.display = "none";

    fileName.textContent =
        "No artwork selected yet ♡";

    detectBtn.disabled = true;

    result.style.display = "none";

    aiBar.style.width = "0%";

    humanBar.style.width = "0%";

    aiPercent.textContent = "0%";

    humanPercent.textContent = "0%";

});
// Detect another image

againBtn.addEventListener("click", function () {

    imageInput.click();

});