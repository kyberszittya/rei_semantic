const path = require('path')
const { wom } = require('maxwhere')
    
function init(props) {
}

function done() {
}

function render(options) {
    wom.addResources(path.resolve(__dirname, 'resources'))
    let szuperkocka = wom.create('canvas', { // render basic in-game Canvas
        width: 800, height: 600, 'resolution-width': 800, 'resolution-height': 600,
        position: {x: -50, y: 0, z: -100},
        physical: {raycast: true}, // accept mouse events to make it orbitable
        done: c => { // paint image in it when it's created
          c.loadPicture('photo.jpg')
        }
      })
    wom.render(szuperkocka)
    
    
                    
    const p1 = { x: -50.0, y: -50.0, z: 0.0 }
    const p2 = { x: -50.0, y: -50.0, z: 0.0 }
    const p3 = { x: -50.0, y: 50.0, z: 0.0 }
    const p4 = { x: -50.0, y: 50.0, z: 0.0 }
    const p5 = { x: 50.0, y: 50.0, z: 0.0 }
    const p6 = { x: 50.0, y: 50.0, z: 0.0 }
    const p7 = { x: 50.0, y: -50.0, z: 0.0 }
    const p8 = { x: 50.0, y: -50.0, z: 0.0 }
    
    const frontFrameSection = {
        material_name: 'Physics/DebugDraw/Red',
        renderop: 'trianglestrap',
        geometry: [
          // 1-2-3
          { type: 'position', arg: p1}, { type: 'position', arg: p2}, { type: 'position', arg: p3},
          // 1-3-4
          { type: 'position', arg: p1}, { type: 'position', arg: p3}, { type: 'position', arg: p4},
          // 1-7-2
          { type: 'position', arg: p1}, { type: 'position', arg: p7}, { type: 'position', arg: p2},
          // 1-8-7
          { type: 'position', arg: p1}, { type: 'position', arg: p8}, { type: 'position', arg: p7},
          // 5-4-3
          { type: 'position', arg: p5}, { type: 'position', arg: p4}, { type: 'position', arg: p3},
          // 5-3-6
          { type: 'position', arg: p5}, { type: 'position', arg: p3}, { type: 'position', arg: p6},
          // 5-6-7
          { type: 'position', arg: p5}, { type: 'position', arg: p6}, { type: 'position', arg: p7},
          // 5-7-8
          { type: 'position', arg: p5}, { type: 'position', arg: p7}, { type: 'position', arg: p8}
        ]
      }
    geom_base_link = [frontFrameSection]

                let base_link = wom.create('manualvisual', {
                    id: 'szuperkocka_base_link',
                    sections: [geom_base_link]
                });
                    

    szuperkocka.appendChild(base_link)
    szuperkocka.render(base_link)
    return <node />
}
module.exports = {
    init,
    done,
    render
}
        