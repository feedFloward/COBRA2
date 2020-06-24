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
    export default {
        name: "classifierSelection",
        data() {
            return {
                classifiers: [],
                selectedClassifier: {}
            }
        },
        created () {
            this.$store.commit('loadClassifierData')
            this.classifiers = this.$store.state.classifiers
        },
        watch: {
            selectedClassifier() {
                this.$store.commit('selectClassifier', this.selectedClassifier)
            }
        },
    }
</script>