let properties = {
    toltalProperties: 0,
}

function addProperty(name, countProp){

    if (name == "vignesh"){
        properties.toltalProperties += countProp;
        return "Properties add to db."
    }

    return "Properties not added. kindly create account."

}

const user1 = addProperty("vignesh", 10)
console.log(user1);
const user2 = addProperty("venkatesh", 5)
console.log(user2);

console.log("Total Properties : "+properties.toltalProperties);