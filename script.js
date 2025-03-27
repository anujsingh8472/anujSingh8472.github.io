fetch('data.json')
    .then(response => response.json())
    .then(data => {
        let examList = document.getElementById("exam-list");
        data.forEach(exam => {
            let li = document.createElement("li");
            li.innerText = `${exam.name} - ${exam.date}`;
            examList.appendChild(li);
        });
    });
