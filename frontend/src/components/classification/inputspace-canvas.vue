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
                if (this.drawMode && Object.keys(this.$store.state.currentClass).length > 0) {
                    this.context.globalAlpha = 0.7;
                    var datapoint_x = tf.randomNormal([1,1], e.offsetX, 7)
                    var datapoint_y = tf.randomNormal([1,1], e.offsetY, 7)
                
                    datapoint_x = datapoint_x.dataSync()[0]
                    datapoint_y = datapoint_y.dataSync()[0]

                    this.$store.commit('addPointsToClass', [datapoint_x, datapoint_y])

                    let color = this.$store.state.currentClass.color

                    this.drawSinglePoint(datapoint_x, datapoint_y, 3, color)
                }
            },
            drawSinglePoint(x, y, size=3, color="Lime") {
                this.context.fillStyle = color
                this.context.beginPath()
                this.context.arc(x, y, size, 0, 2*Math.PI, true)
                this.context.fill()
            },

            redrawCanvas(){
                this.context.globalAlpha = 0.7
                this.context.clearRect(0, 0, this.inputspaceWidth, this.inputspaceHeight)
                let classesData = this.$store.state.classes
                for (let i=0; i< classesData.length; i++) {
                    for (let j=0; j< classesData[i].points.length; j++) {
                        let point = classesData[i].points[j]
                        let color = classesData[i].color
                        this.drawSinglePoint(point[0], point[1], 3, color)
                    }
                }
            }
        },
        mounted () {
            this.context = this.$refs.inputspace_canvas.getContext("2d");
            this.$refs.inputspace_canvas.width = this.inputspaceWidth
            this.$refs.inputspace_canvas.height = this.inputspaceHeight
        },
        computed: {
            numClasses() {
                return this.$store.state.classes.length 
            }
        },
        watch: {
            numClasses: function () {
                this.redrawCanvas()
            }
        },
    }
</script>