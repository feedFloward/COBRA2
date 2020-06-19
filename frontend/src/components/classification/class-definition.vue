<template>
    <div>
        <v-item-group active-class="outlined">
            <v-row>
                <classCard
                v-for="i in classes.length"
                :key="i"
                :classIndex="i"
                class="ml-2 mt-2"
                ></classCard>
            </v-row>
        </v-item-group>
    </div>
</template>

<script>
import classCard from '@/components/classification/class-card'
    export default {
       name: 'classDefinition',
       components: {
           classCard,
       },
       data() {
           return {
           }
       },
       props: {
           classes: {
               type: Array,
               default: () => []
           },
       },
       methods: {
           selectClass() {
               
           }
       },       
       
    }

</script>