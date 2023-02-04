var e = document.documentElement;
if (e.clientWidth > 980) {
    size = 1.8;
} else if (e.clientWidth > 490) {
    size = 2.4;
} else {
    size = 3;
}
e.style.fontSize = size + 'em';
