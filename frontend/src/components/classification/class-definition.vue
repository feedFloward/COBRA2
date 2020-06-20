<template>
    <div>
        <v-item-group> <!-- multiple="false" mandatory -->
            <v-row wrap>
                <classCard
                v-for="cls in classes"
                :key="cls.index"
                :classIndex="cls.index"
                :color="cls.color"
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