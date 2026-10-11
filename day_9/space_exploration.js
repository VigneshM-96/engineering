const starSystems = [
    {name : "Aegis", type: "Terrestrial", distanceY: 4.2, habitable: true},
    {name : "Boreas", type: "Gas Giant", distanceY: 12.5, habitable: false},
    {name : "Cinder", type: "Volcanic", distanceY: 8.1, habitable: false},
    {name : "Dione", type: "Terrestrial", distanceY: 15.0, habitable: true}
]

//map()
const navigationLogs = starSystems.map(planet => `NAV : ${planet.name.toUpperCase()}`);
console.log("\n---1. map() Output (transformed data)---")
console.log(navigationLogs);

//filter()
const habitatPlanets = starSystems.filter(planet => planet.habitable === true)
console.log("\n---2. filter() the habitable Planets only---");
console.log(habitatPlanets);

//find()
const targetPlanet = starSystems.find(planet => planet.name === "Cinder");
console.log("\n---3. find() Output (Single Object Match)---");
console.log(targetPlanet);

//forEach()
console.log("\n---4. forEach() Output (Side Effect Action)---");
starSystems.forEach(planet => {
    console.log(`Probe Trajectory : ${planet.name} is ${planet.distanceY} Light away.`);
});