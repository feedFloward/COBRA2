<template>
    <div>
        <v-card width="inputspaceWidth" height="inputspaceHeight">
            <canvas
            ref="inputspace_canvas"
            @mousedown="drawMode = true"
            @mouseup="drawMode = false"
            @mouseout="drawMode = false"
            @mousemove="brushPoints"
            >
            </canvas>
        </v-card>
    </div>
</template>



<script>

import * as tf from '@tensorflow/tfjs';

    export default {
        name: 'inputspaceCanvas',

        data() {
            return {
                inputspaceHeight: 500,
                inputspaceWidth: 700,
                drawMode: false,
            }
        },

        methods: {
            brushPoints(e) {
                if (this.drawMode) {
                    this.context.globalAlpha = 0.7;
                    var datapoint_x = tf.randomNormal([1,1], e.offsetX, 7)
                    var datapoint_y = tf.randomNormal([1,1], e.offsetY, 7)
                
                    datapoint_x = datapoint_x.dataSync()[0]
                    datapoint_y = datapoint_y.dataSync()[0]

                    this.draw_single_point(datapoint_x, datapoint_y, 3)
                }
            },
            draw_single_point(x, y, size=3, color="Lime") {
                this.context.fillStyle = color
                this.context.beginPath()
                this.context.arc(x, y, size, 0, 2*Math.PI, true)
                this.context.fill()
            },
        },
        mounted () {
            this.context = this.$refs.inputspace_canvas.getContext("2d");
            this.$refs.inputspace_canvas.width = this.inputspaceWidth
            this.$refs.inputspace_canvas.height = this.inputspaceHeight
        },
    }
</script>