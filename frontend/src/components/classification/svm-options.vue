<template>
    <div>
        <v-overflow-btn
        label="choose kernel"
        v-model="specs"
        :items="kernels"
        >
        </v-overflow-btn>
    </div>
</template>

<script>
import { svmSpecs } from '@/store/helpers'

    export default {
        name: 'svmOptions',
        data() {
            return {
                // specs: ''
            }
        },
        computed: {
            ...svmSpecs,

            // das so nochmal überdenken, WENN MÖGLICH IN HELPERS AUSLAGERN!!!!
            specs: {
                get () {
                    return this.$store.state.selectedClassifier.specs.kernel
                },
                set (kernel) {
                    this.$store.commit('chooseKernel', kernel)
                }
            }
        }
    }
</script>