var msnry;

window.addEventListener('load', e => {
    msnry = new Masonry('.grid', {
        columnWidth: 1,
        itemSelector: '.grid-item'
    });
});
