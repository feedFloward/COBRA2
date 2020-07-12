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
import { svmSpecsComputed, svmSpecsMethods } from '@/store/helpers'

    export default {
        name: 'svmOptions',
        data() {
            return {
                // specs: ''
            }
        },
        methods: {
            ...svmSpecsMethods,
        },
        computed: {
            ...svmSpecsComputed,

            // das so nochmal überdenken, WENN MÖGLICH IN HELPERS AUSLAGERN!!!!
            specs: {
                get () {
                    return this.$store.state.selectedClassifier.specs.kernel
                },
                set (kernel) {
                    this.chooseKernel(kernel)
                }
            }
        }
    }
</script>