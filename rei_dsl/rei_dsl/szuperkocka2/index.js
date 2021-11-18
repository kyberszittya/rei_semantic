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
    szuperkocka2.setOrientation({angle: dpos, axis: { x: 0, y: 1.0, z: 1.0 } },'relative', 'parent');
    
}

function render(props, children) {
    wom.addResources(path.resolve(__dirname, 'resources'))

    
    
                
    geom_base_link = rei.createCubeGeometry({ x: -50.0, y: -50.0, z: 50.0 }, 
                    { x: 50.0, y: -50.0, z: 50.0 }, 
                    { x: 50.0, y: 50.0, z: 50.0 },
                    { x: -50.0, y: 50.0, z: 50.0 },
                    { x: 50.0, y: 50.0, z: -50.0 },
                    { x: -50.0, y: 50.0, z: -50.0 },
                    { x: -50.0, y: -50.0, z: -50.0 },
                    { x: 50.0, y: -50.0, z: -50.0 });

        szuperkocka2 = wom.create('manualvisual', {
            id: 'szuperkocka2_base_link',
            sections: geom_base_link
        });
        
                    
    geom_endbox = rei.createCubeGeometry({ x: -25.0, y: -35.0, z: 15.0 }, 
                    { x: 25.0, y: -35.0, z: 15.0 }, 
                    { x: 25.0, y: 35.0, z: 15.0 },
                    { x: -25.0, y: 35.0, z: 15.0 },
                    { x: 25.0, y: 35.0, z: -15.0 },
                    { x: -25.0, y: 35.0, z: -15.0 },
                    { x: -25.0, y: -35.0, z: -15.0 },
                    { x: 25.0, y: -35.0, z: -15.0 });

    let endbox = wom.create('manualvisual', {
        id: 'szuperkocka2_endbox',
        position: {x: 0.0, y: 50.0, z: 0.0 }, 
        orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 },
        sections: geom_endbox
    });
                    
                    
    geom_endbox_tree_1 = rei.createCubeGeometry({ x: -10.0, y: -10.0, z: 10.0 }, 
                    { x: 10.0, y: -10.0, z: 10.0 }, 
                    { x: 10.0, y: 10.0, z: 10.0 },
                    { x: -10.0, y: 10.0, z: 10.0 },
                    { x: 10.0, y: 10.0, z: -10.0 },
                    { x: -10.0, y: 10.0, z: -10.0 },
                    { x: -10.0, y: -10.0, z: -10.0 },
                    { x: 10.0, y: -10.0, z: -10.0 });

    let endbox_tree_1 = wom.create('manualvisual', {
        id: 'szuperkocka2_endbox_tree_1',
        position: {x: 20.0, y: 55.00000000000001, z: 0.0 }, 
        orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 },
        sections: geom_endbox_tree_1
    });
                    
                    
    geom_endbox_tree_2 = rei.createCubeGeometry({ x: -10.0, y: -10.0, z: 10.0 }, 
                    { x: 10.0, y: -10.0, z: 10.0 }, 
                    { x: 10.0, y: 10.0, z: 10.0 },
                    { x: -10.0, y: 10.0, z: 10.0 },
                    { x: 10.0, y: 10.0, z: -10.0 },
                    { x: -10.0, y: 10.0, z: -10.0 },
                    { x: -10.0, y: -10.0, z: -10.0 },
                    { x: 10.0, y: -10.0, z: -10.0 });

    let endbox_tree_2 = wom.create('manualvisual', {
        id: 'szuperkocka2_endbox_tree_2',
        position: {x: -20.0, y: 55.00000000000001, z: 0.0 }, 
        orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 },
        sections: geom_endbox_tree_2
    });
                    
                    
    geom_leg_left = rei.createCubeGeometry({ x: -10.0, y: -120.0, z: 10.0 }, 
                    { x: 10.0, y: -120.0, z: 10.0 }, 
                    { x: 10.0, y: 0.0, z: 10.0 },
                    { x: -10.0, y: 0.0, z: 10.0 },
                    { x: 10.0, y: 0.0, z: -10.0 },
                    { x: -10.0, y: 0.0, z: -10.0 },
                    { x: -10.0, y: -120.0, z: -10.0 },
                    { x: 10.0, y: -120.0, z: -10.0 });

    let leg_left = wom.create('manualvisual', {
        id: 'szuperkocka2_leg_left',
        position: {x: 0.0, y: -50.0, z: 20.0 }, 
        orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 },
        sections: geom_leg_left
    });
                    
                    
    geom_leg_right = rei.createCubeGeometry({ x: -10.0, y: -120.0, z: 10.0 }, 
                    { x: 10.0, y: -120.0, z: 10.0 }, 
                    { x: 10.0, y: 0.0, z: 10.0 },
                    { x: -10.0, y: 0.0, z: 10.0 },
                    { x: 10.0, y: 0.0, z: -10.0 },
                    { x: -10.0, y: 0.0, z: -10.0 },
                    { x: -10.0, y: -120.0, z: -10.0 },
                    { x: 10.0, y: -120.0, z: -10.0 });

    let leg_right = wom.create('manualvisual', {
        id: 'szuperkocka2_leg_right',
        position: {x: 0.0, y: -50.0, z: -20.0 }, 
        orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 },
        sections: geom_leg_right
    });
                    
                geom_appendage_cylinder = rei.createCylinderGeometry(0.2, 1.2, 24, {x: 0.0, y: -0.6, z: 0.0})
    let appendage_cylinder = wom.create('manualvisual', {
        id: 'szuperkocka2_appendage_cylinder',
        position: {x: 40.0, y: 90.0, z: 0.0 }, 
        orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 },
        sections: geom_appendage_cylinder
    });
                    
base_link = szuperkocka2
base_link.appendChild(endbox);
endbox.appendChild(endbox_tree_1);
endbox.appendChild(endbox_tree_2);
base_link.appendChild(leg_left);
base_link.appendChild(leg_right);
endbox.appendChild(appendage_cylinder);
    
    wom.appendChild(szuperkocka2)
    wom.render(szuperkocka2)
    
    
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
        