function processData() {
    const inputData = document.getElementById('data-input').value.trim();
    const bubbleResultsContainer = document.getElementById('bubble-results');
    const mergeResultsContainer = document.getElementById('merge-results');
    const bubbleTimeDisplay = document.getElementById('bubble-time');
    const mergeTimeDisplay = document.getElementById('merge-time');

    if (inputData === "") {
        alert("Masukkan data terlebih dahulu!");
        return;
    }

    const lines = inputData.split("\n");
    const students = [];
    
    // Parsing data input
    for (const line of lines) {
        const [name, score, passingGrade] = line.split(',').map(x => x.trim());
        if (name && score && passingGrade) {
            students.push({ name, score: parseFloat(score), passingGrade: parseFloat(passingGrade) });
        }
    }

    // Sorting algorithms
    function bubbleSort(arr) {
        const start = performance.now();
        const n = arr.length;
        let swapped;
        
        for (let i = 0; i < n - 1; i++) {
            swapped = false;
            for (let j = 0; j < n - 1 - i; j++) {
                if (arr[j].score < arr[j + 1].score) {
                    [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; // Swap
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
        const end = performance.now();
        bubbleTimeDisplay.textContent = (end - start).toFixed(3);
        return arr;
    }

    function mergeSort(arr) {
        const start = performance.now();
        
        if (arr.length <= 1) return arr;

        const mid = Math.floor(arr.length / 2);
        const left = mergeSort(arr.slice(0, mid));
        const right = mergeSort(arr.slice(mid));

        const merged = merge(left, right);

        const end = performance.now();
        mergeTimeDisplay.textContent = (end - start).toFixed(3);
        return merged;
    }

    function merge(left, right) {
        let result = [];
        let i = 0, j = 0;

        while (i < left.length && j < right.length) {
            if (left[i].score > right[j].score) {
                result.push(left[i]);
                i++;
            } else {
                result.push(right[j]);
                j++;
            }
        }
        return result.concat(left.slice(i)).concat(right.slice(j));
    }

    // Applying algorithms to sorted data
    const bubbleSorted = bubbleSort([...students]);
    const mergeSorted = mergeSort([...students]);

    // Displaying the sorted results in two separate tables
    bubbleResultsContainer.innerHTML = generateTable(bubbleSorted);
    mergeResultsContainer.innerHTML = generateTable(mergeSorted);
}

function generateTable(sortedArray) {
    let table = "<table><tr><th>Nama</th><th>Nilai</th><th>Passing Grade</th></tr>";
    sortedArray.forEach(student => {
        table += `<tr><td>${student.name}</td><td>${student.score}</td><td>${student.passingGrade}</td></tr>`;
    });
    table += "</table>";
    return table;
}
