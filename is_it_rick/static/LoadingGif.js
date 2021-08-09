class LoadingGif {
    constructor(parentElement, gifUrl=urls.frontend.assets.loadingGif) {
        this.parent = parentElement;
        this.gifUrl = gifUrl;

        this.element = document.createElement('img');
        this.element.src = this.gifUrl;
        this.parent.append(this.element);
        this.hide();
    }

    show() {
        this.element.style.display = 'initial';
    }

    hide() {
        this.element.style.display = 'none';
    }
}