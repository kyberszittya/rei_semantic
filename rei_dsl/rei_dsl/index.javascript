const path = require('path')
const { wom } = require('maxwhere')
    
function init(props) {
}

function done() {
}

function render(props, children) {
    wom.addResources(path.resolve(__dirname, 'resources'))
    
    
    
            
    const base_link_p1 = { x: -500.0, y: -500.0, z: 500.0 }
    const base_link_p2 = { x: 500.0, y: -500.0, z: 500.0 }
    const base_link_p3 = { x: 500.0, y: 500.0, z: 500.0 }
    const base_link_p4 = { x: -500.0, y: 500.0, z: 500.0 }
    const base_link_p5 = { x: 500.0, y: 500.0, z: -500.0 }
    const base_link_p6 = { x: -500.0, y: 500.0, z: -500.0 }
    const base_link_p7 = { x: -500.0, y: -500.0, z: -500.0 }
    const base_link_p8 = { x: 500.0, y: -500.0, z: -500.0 }
    
    const base_link_frontFrameSection = {
        material_name: 'Physics/DebugDraw/Red',
        renderop: 'trianglestrap',
        geometry: [
          // REAR FACE
          // 1-2-3
          { type: 'position', arg: base_link_p1}, { type: 'position', arg: base_link_p2}, { type: 'position', arg: base_link_p3},
          // 1-3-4
          { type: 'position', arg: base_link_p1}, { type: 'position', arg: base_link_p3}, { type: 'position', arg: base_link_p4},
          // FRONT FACE
          // 5-6-7
          { type: 'position', arg: base_link_p5}, { type: 'position', arg: base_link_p6}, { type: 'position', arg: base_link_p7},
          // 5-7-8
          { type: 'position', arg: base_link_p5}, { type: 'position', arg: base_link_p7}, { type: 'position', arg: base_link_p8},
          // BOTTOM FACE
          // 1-2-8
          { type: 'position', arg: base_link_p1}, { type: 'position', arg: base_link_p2}, { type: 'position', arg: base_link_p8},
          // 1-7-8
          { type: 'position', arg: base_link_p1}, { type: 'position', arg: base_link_p8}, { type: 'position', arg: base_link_p7},
          // LEFT FACE
          // 1-4-6
          { type: 'position', arg: base_link_p1}, { type: 'position', arg: base_link_p4}, { type: 'position', arg: base_link_p6},
          // 1-6-7
          { type: 'position', arg: base_link_p1}, { type: 'position', arg: base_link_p6}, { type: 'position', arg: base_link_p7},
          // RIGHT FACE
          // 2-3-5
          { type: 'position', arg: base_link_p2}, { type: 'position', arg: base_link_p3}, { type: 'position', arg: base_link_p5},
          // 2-5-8
          { type: 'position', arg: base_link_p2}, { type: 'position', arg: base_link_p5}, { type: 'position', arg: base_link_p8},
          // TOP FACE
          // 3-4-5
          { type: 'position', arg: base_link_p3}, { type: 'position', arg: base_link_p4}, { type: 'position', arg: base_link_p5},
          // 4-5-6
          { type: 'position', arg: base_link_p4}, { type: 'position', arg: base_link_p5}, { type: 'position', arg: base_link_p6},
        ]
      }
    geom_base_link = [base_link_frontFrameSection]

        szuperkocka2 = wom.create('manualvisual', {
            id: 'szuperkocka2_base_link',
            sections: geom_base_link
        });
        
                
    const endbox_p1 = { x: -100.0, y: -100.0, z: 100.0 }
    const endbox_p2 = { x: 100.0, y: -100.0, z: 100.0 }
    const endbox_p3 = { x: 100.0, y: 100.0, z: 100.0 }
    const endbox_p4 = { x: -100.0, y: 100.0, z: 100.0 }
    const endbox_p5 = { x: 100.0, y: 100.0, z: -100.0 }
    const endbox_p6 = { x: -100.0, y: 100.0, z: -100.0 }
    const endbox_p7 = { x: -100.0, y: -100.0, z: -100.0 }
    const endbox_p8 = { x: 100.0, y: -100.0, z: -100.0 }
    
    const endbox_frontFrameSection = {
        material_name: 'Physics/DebugDraw/Red',
        renderop: 'trianglestrap',
        geometry: [
          // REAR FACE
          // 1-2-3
          { type: 'position', arg: endbox_p1}, { type: 'position', arg: endbox_p2}, { type: 'position', arg: endbox_p3},
          // 1-3-4
          { type: 'position', arg: endbox_p1}, { type: 'position', arg: endbox_p3}, { type: 'position', arg: endbox_p4},
          // FRONT FACE
          // 5-6-7
          { type: 'position', arg: endbox_p5}, { type: 'position', arg: endbox_p6}, { type: 'position', arg: endbox_p7},
          // 5-7-8
          { type: 'position', arg: endbox_p5}, { type: 'position', arg: endbox_p7}, { type: 'position', arg: endbox_p8},
          // BOTTOM FACE
          // 1-2-8
          { type: 'position', arg: endbox_p1}, { type: 'position', arg: endbox_p2}, { type: 'position', arg: endbox_p8},
          // 1-7-8
          { type: 'position', arg: endbox_p1}, { type: 'position', arg: endbox_p8}, { type: 'position', arg: endbox_p7},
          // LEFT FACE
          // 1-4-6
          { type: 'position', arg: endbox_p1}, { type: 'position', arg: endbox_p4}, { type: 'position', arg: endbox_p6},
          // 1-6-7
          { type: 'position', arg: endbox_p1}, { type: 'position', arg: endbox_p6}, { type: 'position', arg: endbox_p7},
          // RIGHT FACE
          // 2-3-5
          { type: 'position', arg: endbox_p2}, { type: 'position', arg: endbox_p3}, { type: 'position', arg: endbox_p5},
          // 2-5-8
          { type: 'position', arg: endbox_p2}, { type: 'position', arg: endbox_p5}, { type: 'position', arg: endbox_p8},
          // TOP FACE
          // 3-4-5
          { type: 'position', arg: endbox_p3}, { type: 'position', arg: endbox_p4}, { type: 'position', arg: endbox_p5},
          // 4-5-6
          { type: 'position', arg: endbox_p4}, { type: 'position', arg: endbox_p5}, { type: 'position', arg: endbox_p6},
        ]
      }
    geom_endbox = [endbox_frontFrameSection]

                let endbox = wom.create('manualvisual', {
                    id: 'szuperkocka2_endbox',
                    position: {x: 0.0, y: 0.0, z: 150.0 }, 
                    orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 },
                    sections: geom_endbox
                });
                    
base_link = szuperkocka2
        base_link.appendChild(endbox);
    
    wom.appendChild(szuperkocka2)
    wom.render(szuperkocka2)
    return <node />
}
module.exports = {
    init,
    done,
    render
}
        