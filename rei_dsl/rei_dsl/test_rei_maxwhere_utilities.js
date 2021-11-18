const rei_utilities = require('./rei_maxwhere_utilities')
rei = new rei_utilities()

console.log("Testing cube generation")

cyl = rei.createCylinderGeometry(10, 20, 24)
console.log(cyl)

sph = rei.createSphereGeometry(10, 6)
console.log(sph)
