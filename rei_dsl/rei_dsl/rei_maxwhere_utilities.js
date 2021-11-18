function ReiUtilities() {
    // Maxwhere uses centimeters
    base_scale = 100

    this.createCubeGeometry = function(p1, p2, p3, p4, p5, p6, p7, p8){

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

    this.createVector3 = function(fx, fy, fz, offset){
        return { x: fx + offset.x, y: fy + offset.y, z: fz + offset.z }
    }

    this.createCylinderGeometry = function(radius, height, subdiv, offset = {x: 0.0, y: 0.0, z: 0.0}){
        const frontFrameSection = {
            material_name: 'Physics/DebugDraw/VertexDriven',
            renderop: 'trianglestrap',
            geometry: [

            ]
        }
        segment = 2.0 * Math.PI/subdiv
        h = base_scale * height / 2.0
        // Create face
        angle = 0.0
        for (let i = 0; i < subdiv; i++){
            c0_bottom = this.createVector3(
                base_scale * radius * Math.cos(angle),
                -h,
                base_scale * radius * Math.sin(angle), offset)
            c1_bottom = this.createVector3(
                base_scale * radius * Math.cos(angle + segment),
                -h,
                base_scale * radius * Math.sin(angle + segment), offset)
            c0_top = this.createVector3(
                base_scale * radius * Math.cos(angle),
                h,
                base_scale * radius * Math.sin(angle), offset)
            c1_top = this.createVector3(
                base_scale * radius * Math.cos(angle + segment),
                h,
                base_scale * radius * Math.sin(angle + segment), offset)
            frontFrameSection.geometry = frontFrameSection.geometry.concat(
                [
                    // TRI 0
                    { type: 'position', arg: c0_bottom},
                    { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } },
                    { type: 'position', arg: c1_top},
                    { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } },
                    { type: 'position', arg: c1_bottom},
                    { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } },
                    // TRI 1
                    { type: 'position', arg: c0_top},
                    { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } },
                    { type: 'position', arg: c1_top},
                    { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } },
                    { type: 'position', arg: c0_bottom},
                    { type: 'color', arg: { r: 0, g: 0, b: 1, a: 1 } }
                ]
            )
            // Increment angle
            angle += segment
        }
        // Create bottom disc
        angle = 0.0

        for (let i = 0; i < subdiv; i++){
            cp = this.createVector3(0.0, -h, 0.0, offset)
            c1 = this.createVector3(
                base_scale * radius * Math.cos(angle),
                -h,
                base_scale* radius * Math.sin(angle), offset)
            c2 = this.createVector3(
                base_scale * radius * Math.cos(angle + segment),
                -h,
                base_scale * radius * Math.sin(angle + segment), offset)
            frontFrameSection.geometry = frontFrameSection.geometry.concat(
                [
                    { type: 'position', arg: c1},
                    { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
                    { type: 'position', arg: c2},
                    { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
                    { type: 'position', arg: cp},
                    { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } }
                ]
            )
            // Increment angle
            angle += segment
        }
        // Create top disc
        angle = 0.0
        for (let i = 0; i < subdiv; i++){
            cp = this.createVector3(0.0, h, 0.0, offset)
            c1 = this.createVector3(
                base_scale * radius * Math.cos(angle),
                h,
                base_scale* radius * Math.sin(angle), offset)
            c2 = this.createVector3(
                base_scale * radius * Math.cos(angle + segment),
                h,
                base_scale * radius * Math.sin(angle + segment), offset)
            frontFrameSection.geometry = frontFrameSection.geometry.concat(
                [
                    { type: 'position', arg: c2},
                    { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
                    { type: 'position', arg: c1},
                    { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
                    { type: 'position', arg: cp},
                    { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } }
                ]
            )
            // Increment angle
            angle += segment
        }
        // Return
        return [frontFrameSection]
    }

    this.createSphereGeometry = function(radius, subdiv, offset = {x: 0.0, y: 0.0, z: 0.0}) {
        const frontFrameSection = {
            material_name: 'Physics/DebugDraw/VertexDriven',
            renderop: 'trianglestrap',
            geometry: [

            ]
        }
        segment = 2.0 * Math.PI/subdiv
        seg_theta = Math.PI/subdiv
        // Faces
        theta = 0.0
        for (let i = 0; i < subdiv; i++){
            angle = 0.0
            for (let j = 0; j < subdiv; j++){
                c0_0 = this.createVector3(
                    base_scale * radius * Math.cos(angle) * Math.sin(theta),
                    base_scale * radius * Math.cos(theta),
                    base_scale * radius * Math.sin(angle) * Math.sin(theta), offset)
                c0_1 = this.createVector3(
                    base_scale * radius * Math.cos(angle + segment) * Math.sin(theta),
                    base_scale * radius * Math.cos(theta),
                    base_scale * radius * Math.sin(angle + segment) * Math.sin(theta), offset)
                c1_0 = this.createVector3(
                    base_scale * radius * Math.cos(angle) * Math.sin(theta + seg_theta),
                    base_scale * radius * Math.cos(theta + seg_theta),
                    base_scale * radius * Math.sin(angle) * Math.sin(theta + seg_theta), offset)
                c1_1 = this.createVector3(
                    base_scale * radius * Math.cos(angle + segment) * Math.sin(theta + seg_theta),
                    base_scale * radius * Math.cos(theta + seg_theta),
                    base_scale * radius * Math.sin(angle + segment) * Math.sin(theta + seg_theta), offset)
                frontFrameSection.geometry = frontFrameSection.geometry.concat(
                    [
                        // TRI 0
                        { type: 'position', arg: c0_1},
                        { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
                        { type: 'position', arg: c1_0},
                        { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
                        { type: 'position', arg: c1_1},
                        { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
                        // TRI 1
                        { type: 'position', arg: c0_0},
                        { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
                        { type: 'position', arg: c1_0},
                        { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } },
                        { type: 'position', arg: c0_1},
                        { type: 'color', arg: { r: 0, g: 1, b: 0, a: 1 } }
                    ]
                )
                angle += segment
            }
            theta += seg_theta
        }
        // Return
        return [frontFrameSection]
    }
}

module.exports = ReiUtilities;