const userProfile = {
    userName: "Vignesh",
    xp: 80,
    badges: ["HTML Mastered", "CSS Ninja"]
}

function awardNewBadge(profile, scoreNeeded, newBadge){
    if (profile.xp >= scoreNeeded && !profile.badges.includes(newBadge)){
        profile.badges.push(newBadge);
        profile.xp += 15;
        return`Congratulations! You earned the [${newBadge}] badge.`;
    }

    return `Criteria not met badge already owned`
}

console.log("---Initial Profile ---", userProfile);

const levelUp = awardNewBadge(userProfile, 80, "Python Legend");
console.log(levelUp);

const failedAttempt = awardNewBadge(userProfile, 200, "Cloud Architect");
console.log(failedAttempt);