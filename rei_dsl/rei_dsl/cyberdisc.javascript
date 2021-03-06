module.exports = {
    resources: `${__dirname}/resources`,
    init() {
    },
    done() {
    },
    render(options) {
        
        cyberdisc = wom.create(('mesh'), {url: 'pendulum_kocsi.mesh', position: conf.cart.position, orientation: conf.cart.orientation, scale: conf.cart.scale, autophysical: false});

        let base_link = wom.create('mesh', {
            ('', '{url:, position: {x: 0.0, y: 0.0, z: 0.0 }, orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 }, scale: 100, autophysics: true  }')
        });
            
        let motor_0_motor_root = wom.create('mesh', {
            ('', '{url:, position: {x: 0.1, y: 0.1, z: 0.0 }, orientation: {w: 0.7071067811865476, x: 0.0, y: 0.0, z: 0.7071067811865476 }, scale: 100, autophysics: true  }')
        });
            
        let motor_0_motor_axle = wom.create('mesh', {
            ('', '{url:, position: {x: 0.04, y: 0.0, z: 0.0 }, orientation: {w: 0.7071067811865476, x: 0.0, y: 0.7071067811865476, z: 0.0 }, scale: 100, autophysics: true  }')
        });
            
        let motor_0_wheel_link = wom.create('mesh', {
            ('', '{url:, position: {x: 0.0, y: 0.0, z: 0.0 }, orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 }, scale: 100, autophysics: true  }')
        });
            
        let motor_1_motor_root = wom.create('mesh', {
            ('', '{url:, position: {x: -0.1, y: 0.1, z: 0.0 }, orientation: {w: 0.7071067811865476, x: 0.0, y: 0.0, z: 0.7071067811865476 }, scale: 100, autophysics: true  }')
        });
            
        let motor_1_motor_axle = wom.create('mesh', {
            ('', '{url:, position: {x: 0.04, y: 0.0, z: 0.0 }, orientation: {w: 0.7071067811865476, x: 0.0, y: 0.7071067811865476, z: 0.0 }, scale: 100, autophysics: true  }')
        });
            
        let motor_1_wheel_link = wom.create('mesh', {
            ('', '{url:, position: {x: 0.0, y: 0.0, z: 0.0 }, orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 }, scale: 100, autophysics: true  }')
        });
            
        let motor_2_motor_root = wom.create('mesh', {
            ('', '{url:, position: {x: -0.1, y: -0.1, z: 0.0 }, orientation: {w: 0.7071067811865476, x: 0.0, y: 0.0, z: -0.7071067811865476 }, scale: 100, autophysics: true  }')
        });
            
        let motor_2_motor_axle = wom.create('mesh', {
            ('', '{url:, position: {x: 0.04, y: 0.0, z: 0.0 }, orientation: {w: 0.7071067811865476, x: 0.0, y: 0.7071067811865476, z: 0.0 }, scale: 100, autophysics: true  }')
        });
            
        let motor_2_wheel_link = wom.create('mesh', {
            ('', '{url:, position: {x: 0.0, y: 0.0, z: 0.0 }, orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 }, scale: 100, autophysics: true  }')
        });
            
        let motor_3_motor_root = wom.create('mesh', {
            ('', '{url:, position: {x: 0.1, y: -0.1, z: 0.0 }, orientation: {w: 0.7071067811865476, x: 0.0, y: 0.0, z: -0.7071067811865476 }, scale: 100, autophysics: true  }')
        });
            
        let motor_3_motor_axle = wom.create('mesh', {
            ('', '{url:, position: {x: 0.04, y: 0.0, z: 0.0 }, orientation: {w: 0.7071067811865476, x: 0.0, y: 0.7071067811865476, z: 0.0 }, scale: 100, autophysics: true  }')
        });
            
        let motor_3_wheel_link = wom.create('mesh', {
            ('', '{url:, position: {x: 0.0, y: 0.0, z: 0.0 }, orientation: {w: 1.0, x: 0.0, y: 0.0, z: 0.0 }, scale: 100, autophysics: true  }')
        });
            
        motor_0_motor_root.appendChild(motor_0_motor_axle);
        motor_0_motor_axle.appendChild(motor_0_wheel_link);
        base_link.appendChild(motor_0_motor_root);
        motor_1_motor_root.appendChild(motor_1_motor_axle);
        motor_1_motor_axle.appendChild(motor_1_wheel_link);
        base_link.appendChild(motor_1_motor_root);
        motor_2_motor_root.appendChild(motor_2_motor_axle);
        motor_2_motor_axle.appendChild(motor_2_wheel_link);
        base_link.appendChild(motor_2_motor_root);
        motor_3_motor_root.appendChild(motor_3_motor_axle);
        motor_3_motor_axle.appendChild(motor_3_wheel_link);
        base_link.appendChild(motor_3_motor_root);

        cyberdisc.appendChild(base_link);

        wom.render(cyberdisc);
    }
}
        