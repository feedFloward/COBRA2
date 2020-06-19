<template>
    <div>
        <v-item v-slot:default="{ active, toggle }">
        <v-card
        width="100"
        height="70"
        :color= "color"
        class="lighten-5"
        @click="toggle"
        >
            <v-card-text>
                <p>class {{ classIndex }}</p>
                <p>#samples</p>
                <p v-if="active">aktiv</p>
            </v-card-text>
        </v-card>
        </v-item>
    </div>
</template>

<script>
import {colorMap} from '../../shared'
    export default {
        name: 'classCard',
        props: {
            classIndex: {
                type: Number,
            },
        },
        data() {
            return {
                color: undefined
            }
        },
        mounted () {
            this.color = colorMap[this.classIndex];
        },
    }
</script>