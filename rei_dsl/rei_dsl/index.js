const path = require('path')
const { wom } = require('maxwhere')
// Connection with server side
const io = require('./socket.io.min.js');
// REI-utilities
const reiutilities = require('./rei_maxwhere_utilities.js');
const rei = new reiutilities();

var tickObj = null;


const socket = io();

function init(props) {
}

function done() {
}

var control_tick = function() {
    dpos = 0.1;
    szuperhenger.setOrientation({angle: dpos, axis: { x: 0, y: 1.0, z: 1.0 } },'relative', 'parent');
    
}

function render(props, children) {
    wom.addResources(path.resolve(__dirname, 'resources'))

    
    
            geom_base_link = rei.createSphereGeometry(0.5, 6, {x: 0.0, y: 0.0, z: 0.0})
        szuperhenger = wom.create('manualvisual', {
            id: 'szuperhenger_base_link',
            sections: geom_base_link
        });
        
base_link = szuperhenger
    
    wom.appendChild(szuperhenger)
    wom.render(szuperhenger)
    
    
    if (tickObj==null){
        tickObj = setInterval(control_tick, 50);
    }
    

    return <node />
}
module.exports = {
    init,
    done,
    render
}
        