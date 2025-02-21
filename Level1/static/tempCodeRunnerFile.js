const questions = [
    { type: "capital", question: "What is the capital of {country}?", answerKey: "capital_city" },
    { type: "country_from_capital", question: "Which country has {capital} as its capital?", answerKey: "country_name" },
    { type: "currency", question: "What is the currency of {country}?", answerKey: "currency" },
    { type: "landmark", question: "Which landmark is in {country}?", answerKey: "landmarks" },
    { type: "country_from_landmark", question: "Which country has this landmark: {landmark}?", answerKey: "country_name" }
];

let questionCount = 0;
const maxQuestions = 10;
let correctAnswer = "";

async function fetchData() {
    const response = await fetch('/static/Countries.json'); // Convert CSV to JSON manually
    return await response.json();
}

async function nextQuestion() {
    if (questionCount >= maxQuestions) {
        document.getElementById("question").innerText = "🎉 Quiz Over! Well done!";
        document.getElementById("options").innerHTML = "";
        return;
    }

    questionCount++;
    const data = await fetchData();
    const questionType = questions[Math.floor(Math.random() * questions.length)];
    const randomCountry = data[Math.floor(Math.random() * data.length)];

    let questionText = questionType.question
        .replace("{country}", randomCountry.country_name)
        .replace("{capital}", randomCountry.capital_city)
        .replace("{landmark}", randomCountry.landmarks);

    correctAnswer = randomCountry[questionType.answerKey];

    let options = data.map(item => item[questionType.answerKey]).filter(Boolean);
    let wrongAnswers = options.filter(opt => opt !== correctAnswer).sort(() => 0.5 - Math.random()).slice(0, 3);
    let allAnswers = [...wrongAnswers, correctAnswer].sort(() => 0.5 - Math.random());

    document.getElementById("question").innerText = `Question ${questionCount}/${maxQuestions}: ${questionText}`;
    document.getElementById("options").innerHTML = allAnswers.map(answer =>
        `<button onclick="checkAnswer('${answer}')">${answer}</button>`).join(" ");
}

function checkAnswer(answer) {
    document.getElementById("result").innerText = answer === correctAnswer ? "✅ Correct!" : "❌ Wrong! Try again.";
    setTimeout(nextQuestion, 2000);
}

nextQuestion();
