function refreshImage() {
    if (state.pid === "") return;

    let src = `http://localhost:5000/get_plot?pid=${state.pid}&date=${new Date().valueOf()}`

    if (state.start !== "") src += `start=${convertTime(state.start)}`;
    if (state.end !== "") src += `end=${convertTime(state.end)}`;

    document.getElementById("memUsageImage").src = src;
}

function convertTime(timeStr) {
    if (timeStr.length === 0) return '';

    const value = parseFloat(timeStr.slice(0, -1), 10);

    if (value == NaN) {
        return '';
    }

    const lastChar = timeStr[timeStr.length - 1];

    switch (lastChar) {
        case 'h': return value * 60 * 60;
        case 'm': return value * 60;
        default:
            return value;
    }
}

function setState(field, value) {
    state[field] = event.target.value;

    localStorage.setItem("state", JSON.stringify(state));
}

const state = {
    pid: '',
    start: '',
    end: '',
    ...JSON.parse(localStorage.getItem("state"))
};

setInterval(refreshImage, 2000);

document.getElementById("pidInput").onchange = event => setState("pid", event.target.value);
document.getElementById("pidInput").value = state.pid

document.getElementById("startInput").onchange = event => setState("start", event.target.value);
document.getElementById("startInput").value = state.start

document.getElementById("endInput").onchange = event => setState("end", event.target.value);
document.getElementById("endInput").value = state.end
