class Plants {
    constructor() {}
    getPlants() {
        return $.get("/plants");
    }
}
