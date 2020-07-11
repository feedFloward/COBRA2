import { mapState, mapActions } from 'vuex'
import { ClfState } from '@/types/classification'

export const svmSpecs = {
    ...mapState({
        kernels: (state) => (state as ClfState).modelSpecData.svmSpecs.kernel,

    }),
}