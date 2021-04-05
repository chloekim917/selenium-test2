document.addEventListener("DOMContentLoaded", () => {
    getWordsCount()
})

//fetch word count from api
function getWordsCount(){
    fetch('http://localhost:5000')
    .then(resp => resp.json())
    // .then(console.log)
    .then(wordsCount =>
    renderWordsCount(wordsCount)
    )
}

//make a list of words and the count
function renderWordsCount(wordsCount){
    const counter = document.querySelector('.words-count')
    wordsCount.words.forEach(word => {
        counter.innerHTML += `
          <li>${word}</li>`
    });
}
