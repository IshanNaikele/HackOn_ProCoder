let quizData = [];
let availableQuestions = [];
let currentQuestion = {};
let correctAnswer = "";

// Load quiz data
fetch("quiz_data.json")
    .then(response => response.json())
    .then(data => {
        quizData = [...data];
        availableQuestions = [...quizData]; // Copy for tracking
        loadQuestion();
    });

// Load a new question without repetition
function loadQuestion() {
    if (availableQuestions.length === 0) {
        availableQuestions = [...quizData]; // Reset questions when all are asked
    }

    let randomIndex = Math.floor(Math.random() * availableQuestions.length);
    currentQuestion = availableQuestions.splice(randomIndex, 1)[0]; // Remove asked question
    correctAnswer = currentQuestion.capital_city;

    document.getElementById("question").innerText = `What is the capital of ${currentQuestion.country_name}?`;

    let options = [correctAnswer, ...getWrongAnswers()];
    options.sort(() => Math.random() - 0.5);

    let buttons = document.querySelectorAll(".option-btn");
    buttons.forEach((btn, i) => {
        btn.innerText = options[i];
        btn.style.background = "white";
        btn.disabled = false;
    });

    document.getElementById("result").innerText = "";
}

// Get 3 wrong answers
function getWrongAnswers() {
    let wrongAnswers = quizData
        .map(q => q.capital_city)
        .filter(capital => capital !== correctAnswer);
    
    return wrongAnswers.sort(() => Math.random() - 0.5).slice(0, 3);
}

// Check answer
function checkAnswer(btn) {
    if (btn.innerText === correctAnswer) {
        btn.style.background = "green";
        document.getElementById("result").innerText = "✅ Correct!";
        setTimeout(loadQuestion, 2000);
    } else {
        btn.style.background = "red";
        document.getElementById("result").innerText = "❌ Wrong! Try again.";
    }

    document.querySelectorAll(".option-btn").forEach(button => button.disabled = true);
}
