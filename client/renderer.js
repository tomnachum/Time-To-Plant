class Renderer {
    constructor() {}

    render(plants) {
        const source = $("#plants-template").html();
        const template = Handlebars.compile(source);
        let newHTML = template({ plants: plants });
        $(".plants").empty();
        $(".plants").append(newHTML);
    }
}
