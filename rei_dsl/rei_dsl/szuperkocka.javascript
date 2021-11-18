const path = require('path')
const { wom } = require('maxwhere')
const io = require('./socket.io.min.js');


function getCubeGeometry(p1, p2, p3, p4, p5, p6, p7, p8){
    
    const frontFrameSection = {
        material_name: 'Physics/DebugDraw/VertexDriven',
        renderop: 'trianglestrap',
        geometry: [
          // REAR FACE
          // 1-2-3
          { type: 'position', arg: p1},
          { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
          { type: 'position', arg: p2},
          { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
          { type: 'position', arg: p3},
          { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
          // 1-3-4
          { type: 'position', arg: p1},
          { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
          { type: 'position', arg: p3},
          { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
          { type: 'position', arg: p4},
          { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
          // FRONT FACE
          // 5-6-7
          { type: 'position', arg: p7},
          { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } },
          { type: 'position', arg: p6},
          { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } },
          { type: 'position', arg: p5},
          { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } },
          // 5-7-8
          { type: 'position', arg: p8},
          { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } },
          { type: 'position', arg: p7},
          { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } },
          { type: 'position', arg: p5},
          { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } },
          // BOTTOM FACE
          // 1-2-8
          { type: 'position', arg: p8},
          { type: 'color', arg: { r: 1, g: 1, b: 1, a: 1 } },
          { type: 'position', arg: p2},
          { type: 'color', arg: { r: 1, g: 1, b: 1, a: 1 } },
          { type: 'position', arg: p1},
          { type: 'color', arg: { r: 1, g: 1, b: 1, a: 1 } },
          // 1-7-8
          { type: 'position', arg: p7},
          { type: 'color', arg: { r: 1, g: 1, b: 1, a: 1 } },
          { type: 'position', arg: p8},
          { type: 'color', arg: { r: 1, g: 1, b: 1, a: 1 } },
          { type: 'position', arg: p1},
          { type: 'color', arg: { r: 1, g: 1, b: 1, a: 1 } },
          // LEFT FACE
          // 1-4-6
          { type: 'position', arg: p1},
          { type: 'color', arg: { r: 1, g: 0, b: 0, a: 1 } },
          { type: 'position', arg: p4},
          { type: 'color', arg: { r: 1, g: 0, b: 0, a: 1 } },
          { type: 'position', arg: p6},
          { type: 'color', arg: { r: 1, g: 0, b: 0, a: 1 } },
          // 1-6-7
          { type: 'position', arg: p1},
          { type: 'color', arg: { r: 1, g: 0, b: 0, a: 1 } },
          { type: 'position', arg: p6},
          { type: 'color', arg: { r: 1, g: 0, b: 0, a: 1 } },
          { type: 'position', arg: p7},
          { type: 'color', arg: { r: 1, g: 0, b: 0, a: 1 } },
          // RIGHT FACE
          // 2-3-5
          { type: 'position', arg: p5}, 
          { type: 'color', arg: { r: 1, g: 0, b: 1, a: 1 } },
          { type: 'position', arg: p3}, 
          { type: 'color', arg: { r: 1, g: 0, b: 1, a: 1 } },
          { type: 'position', arg: p2},
          { type: 'color', arg: { r: 1, g: 0, b: 1, a: 1 } },
          // 2-5-8
          { type: 'position', arg: p8}, 
          { type: 'color', arg: { r: 1, g: 0, b: 1, a: 1 } },
          { type: 'position', arg: p5}, 
          { type: 'color', arg: { r: 1, g: 0, b: 1, a: 1 } },
          { type: 'position', arg: p2},
          { type: 'color', arg: { r: 1, g: 0, b: 1, a: 1 } },
          // TOP FACE
          // 3-4-5
          { type: 'position', arg: p5}, 
          { type: 'color', arg: { r: 0, g: 1, b: 1, a: 1 } },          
          { type: 'position', arg: p4}, 
          { type: 'color', arg: { r: 0, g: 1, b: 1, a: 1 } },
          { type: 'position', arg: p3},
          { type: 'color', arg: { r: 0, g: 1, b: 1, a: 1 } },
          // 4-5-6
          { type: 'position', arg: p4}, 
          { type: 'color', arg: { r: 0, g: 1, b: 1, a: 1 } },
          { type: 'position', arg: p5}, 
          { type: 'color', arg: { r: 0, g: 1, b: 1, a: 1 } },
          { type: 'position', arg: p6},
          { type: 'color', arg: { r: 0, g: 1, b: 1, a: 1 } },
        ]
      }
    return [frontFrameSection]

}
    

const socket = io();

function init(props) {
}

function done() {
}

function render(props, children) {
    wom.addResources(path.resolve(__dirname, 'resources'))
    
                
    geom_base_link = getCubeGeometry({ x: -50.0, y: -50.0, z: 50.0 }, 
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
        
                    
    geom_endbox = getCubeGeometry({ x: -25.0, y: -35.0, z: 15.0 }, 
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
                    
                    
    geom_endbox_tree_1 = getCubeGeometry({ x: -10.0, y: -10.0, z: 10.0 }, 
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
                    
                    
    geom_endbox_tree_2 = getCubeGeometry({ x: -10.0, y: -10.0, z: 10.0 }, 
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
                    
                    
    geom_leg_left = getCubeGeometry({ x: -10.0, y: -60.0, z: 10.0 }, 
                    { x: 10.0, y: -60.0, z: 10.0 }, 
                    { x: 10.0, y: 60.0, z: 10.0 },
                    { x: -10.0, y: 60.0, z: 10.0 },
                    { x: 10.0, y: 60.0, z: -10.0 },
                    { x: -10.0, y: 60.0, z: -10.0 },
                    { x: -10.0, y: -60.0, z: -10.0 },
                    { x: 10.0, y: -60.0, z: -10.0 });

    let leg_left = wom.create('manualvisual', {
        id: 'szuperkocka2_leg_left',
        position: {x: 0.0, y: -50.0, z: 20.0 }, 
        orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 },
        sections: geom_leg_left
    });
                    
                    
    geom_leg_right = getCubeGeometry({ x: -10.0, y: -60.0, z: 10.0 }, 
                    { x: 10.0, y: -60.0, z: 10.0 }, 
                    { x: 10.0, y: 60.0, z: 10.0 },
                    { x: -10.0, y: 60.0, z: 10.0 },
                    { x: 10.0, y: 60.0, z: -10.0 },
                    { x: -10.0, y: 60.0, z: -10.0 },
                    { x: -10.0, y: -60.0, z: -10.0 },
                    { x: 10.0, y: -60.0, z: -10.0 });

    let leg_right = wom.create('manualvisual', {
        id: 'szuperkocka2_leg_right',
        position: {x: 0.0, y: -50.0, z: -20.0 }, 
        orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 },
        sections: geom_leg_right
    });
                    
base_link = szuperkocka2
base_link.appendChild(endbox);
endbox.appendChild(endbox_tree_1);
endbox.appendChild(endbox_tree_2);
base_link.appendChild(leg_left);
base_link.appendChild(leg_right);
    
    wom.appendChild(szuperkocka2)
    wom.render(szuperkocka2)
    
    var tick = function() {
        dpos = 0.1;
        szuperkocka2.setOrientation({angle: dpos, axis: { x: 0, y: 1.0, z: 1.0 } },'relative', 'parent');
        endbox.setOrientation({angle: dpos, axis: { x: 0, y: 1.0, z: 1.0 } },'relative', 'parent');
endbox_tree_1.setOrientation({angle: dpos, axis: { x: 0, y: 1.0, z: 1.0 } },'relative', 'parent');
endbox_tree_2.setOrientation({angle: dpos, axis: { x: 0, y: 1.0, z: 1.0 } },'relative', 'parent');
leg_left.setOrientation({angle: dpos, axis: { x: 0, y: 1.0, z: 1.0 } },'relative', 'parent');
leg_right.setOrientation({angle: dpos, axis: { x: 0, y: 1.0, z: 1.0 } },'relative', 'parent');

    }
    tickObj = setInterval(tick, 50);

    return <node />
}
module.exports = {
    init,
    done,
    render
}
        