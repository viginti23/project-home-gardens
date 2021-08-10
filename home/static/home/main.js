const sideImages = document.querySelectorAll('.sideImages img');
const wrapperImageZom = document.querySelector('.imageZoom');

document.addEventListener('DOMContentLoaded', () => {
    wrapperImageZom.style.backgroundImage = `url(${sideImages[0].src})`;
});

sideImages.forEach((img) => {
    img.addEventListener('click', () => {
        wrapperImageZom.style.backgroundImage = `url(${img.src})`;
    });
});

wrapperImageZom.addEventListener('mousemove', (e) => {
    const clientRect = wrapperImageZom.getBoundingClientRect();
    const posXZero = e.clientX - clientRect.left;
    const posYZero = e.clientY - clientRect.top;
    const posXMouse = Math.round(100 / (clientRect.width / posXZero));
    const posYMouse = Math.round(100 / (clientRect.height / posYZero));

    wrapperImageZom.style.backgroundSize = '250% 250%';
    wrapperImageZom.style.backgroundPosition = `${posXMouse}% ${posYMouse}%`;
});

wrapperImageZom.addEventListener('mouseleave', () => {
    wrapperImageZom.style.backgroundSize = '100% 100%';
    wrapperImageZom.style.backgroundPosition = '100% 100%';
});
