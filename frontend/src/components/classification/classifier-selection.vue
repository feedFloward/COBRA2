<template>
    <div>
        <v-overflow-btn
        :items="classifiers"
        label="choose classifier"
        v-model="selectedClassifier"
        ></v-overflow-btn>
    </div>
</template>

<script>
import { classifierSelectionMethods, classifierSelectionComputed } from '@/store/helpers'
    export default {
        name: "classifierSelection",
        data() {
            return {
                selectedClassifier: {}
            }
        },
        methods: {
            ...classifierSelectionMethods,
        },
        computed: {
            ...classifierSelectionComputed,
        },
        created () {
            this.loadClassifierData()
        },
        watch: {
            selectedClassifier() {
                this.selectClassifier(this.selectedClassifier)
            }
        },
    }
</script>