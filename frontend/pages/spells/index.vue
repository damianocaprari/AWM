<template>
  <v-container>
    <v-row>
      <v-col class="d-sm-none">
        <h2>Spells</h2>
      </v-col>
      <!-- for screen >= 600 px -->
      <v-col class="d-none d-sm-block">
        <h1>Spells</h1>
      </v-col>

      <template v-if="isLogged()">
        <!-- for screen < 600 px -->
        <v-col class="d-sm-none" align="right">
          <v-btn right color="primary" to="/spells/add" small>Add spell</v-btn>
        </v-col>
        <!-- for screen >= 600 px -->
        <v-col class="d-none d-sm-block" align="right">
          <v-btn right color="primary" to="/spells/add">Add spell</v-btn>
        </v-col>
      </template>

    </v-row>

    <spells-table :spells="spells" :spelltags="spelltags" :characterclasses="characterclasses"></spells-table>

  </v-container>

</template>


<script>
    import SpellsTable from "~/components/SpellsTable";

    export default {
        head() {
            return {
                title: "AWM Project - Spells",
            };
        },

        components: {
            SpellsTable,
        },

        async asyncData({$axios, params}) {
            let retval = {spells: [], characterclasses: [], spelltags: []}
            try {
                let query_spells = await $axios.$get(`/spells/`);
                let query_characterclasses = await $axios.$get(`/characterclasses/`);
                let query_spelltags = await $axios.$get(`/spelltags/`);

                console.log(query_spells)

                if (query_spells.count > 0) {
                    retval.spells = query_spells.results
                    // -- Add casting_time value
                    retval.spells.forEach(spell => {
                        let casting_time = "" + spell.casting_time_amount + " " + spell.casting_time_unit.toLowerCase()
                        spell['casting_time'] = casting_time
                    })

                    // -- Add tags in spells
                    retval.spells.forEach(spell => {
                        if (spell.spell_additional_info != null) {
                            if (spell.spell_additional_info.tags != null) {
                                // let tag_list = "" + spell.spell_additional_info.tags[0].tag
                                let tag_list = ""
                                for (var cnt in spell.spell_additional_info.tags) {
                                    tag_list = tag_list.concat(spell.spell_additional_info.tags[cnt].tag)
                                    tag_list = tag_list.concat(" ")
                                }
                                spell['tag_list'] = tag_list.trim()
                            } else
                                spell['tag_list'] = '-'
                        } else {
                            spell['tag_list'] = '-'
                        }
                    })

                    // -- Add classes name in spells
                    retval.spells.forEach(spell => {
                        if (spell.classes != null) {
                            let class_list = ""
                            for (var cnt in spell.classes) {
                                for (var cl in query_characterclasses.results) {
                                    var a = query_characterclasses.results[cl].url
                                    if (a.match(spell.classes[cnt])) {
                                        class_list = class_list.concat(query_characterclasses.results[cl].name)
                                        class_list = class_list.concat(" ")
                                    }
                                }
                            }
                            spell['class_list'] = class_list
                        }
                    })
                }

                if (query_spelltags.count > 0) {
                    let v = {text: "All", value: null}
                    retval.spelltags.push(v)
                    for (var i = 0; i < query_spelltags.count; i++) {
                        let v = {text: query_spelltags.results[i].tag, value: query_spelltags.results[i].tag}
                        retval.spelltags.push(v)
                    }
                }

                if (query_characterclasses.count > 0) {
                    let v = {text: "All", value: null}
                    retval.characterclasses.push(v)
                    for (var i = 0; i < query_characterclasses.count; i++) {
                        let v = {
                            text: query_characterclasses.results[i].name,
                            value: query_characterclasses.results[i].name
                        }
                        retval.characterclasses.push(v)
                    }
                }

            } catch (e) {
                console.log(e);
            }
            return retval
        },

        data() {
            return {
                spells: [],
                search: '',
                search_desc: '',
                search_lvl: '',
                search_class: '',
                characterclasses: [],

                levelsList: [
                    {text: "All", value: null},
                    {text: "Cantrip", value: 0},
                    {text: "1st", value: 1},
                    {text: "2nd", value: 2},
                    {text: "3th", value: 3},
                    {text: "4th", value: 4},
                    {text: "5th", value: 5},
                    {text: "6th", value: 6},
                    {text: "7th", value: 7},
                    {text: "8th", value: 8},
                    {text: "9th", value: 9},
                ],

                // Filter models
                spellFilterValue: '',
                levelsFilterValue: null,
                spelltagsFilterValue: null,
                characterclassesFilterValue: null,

                // v-data-table
                headers: [
                    {text: 'LEVEL', value: 'level', align: 'left', filter: this.levelsFilter},
                    {text: 'NAME', value: 'name', align: 'center', filter: this.nameFilter,},
                    {text: 'CASTING TIME', value: 'casting_time', align: 'center', sortable: false},
                    {text: 'TAGS', value: 'tag_list', align: 'center', filter: this.spelltagsFilter},
                    {text: 'CLASSES', value: 'class_list', align: ' d-none', filter: this.characterclassesFilter},
                    {text: ' ', value: 'data-table-expand', align: 'left'}
                ],
                expanded: [],
                // For filters
                spelltags: [],       // For tags
            };
        },

        methods: {
            async deleteSpell(spell_id) {
                try {
                    await this.$axios.$delete(`/spells/${spell_id}/`); // delete spell
                    let newSpell = await this.$axios.$get("/spells/"); // get new list of cspells
                    this.spells = newSpells; // update list of spells
                } catch (e) {
                    console.log(e);
                }
            },

            onScroll(e) {
                if (typeof window === 'undefined')
                    return
                const top = window.pageYOffset || e.target.scrollTop || 0
                this.fab = top > 20
            },
            toTop() {
                this.$vuetify.goTo(0)
            },

            // ----- NEW FILTER -----
            // -- Filter for spell name col
            nameFilter(value) {
                if (!this.spellFilterValue) {
                    return true;
                }
                return value.toLowerCase().includes(this.spellFilterValue.toLowerCase());
            },

            // -- Filter for level col
            levelsFilter(value) {
                if (!this.levelsFilterValue) {
                    return true;
                }
                return value == this.levelsFilterValue;
            },

            // -- Filter for spell tags col
            spelltagsFilter(value) {
                if (!this.spelltagsFilterValue) {
                    return true;
                }
                return value.toLowerCase().includes(this.spelltagsFilterValue.toLowerCase());
            },

            // -- Filter for character classes
            characterclassesFilter(value) {
                if (!this.characterclassesFilterValue) {
                    return true;
                }
                return value.toLowerCase().includes(this.characterclassesFilterValue.toLowerCase());
            },

            // Expand row
            expandRow(item) {
                this.expanded = item == this.expanded[0] ? [] : [item]
            },

            isLogged() {
                try {
                    let user = this.$store.state.auth.user
                    if (!!user) {
                        return true
                    }
                } catch (e) {
                    console.log('spells/add isLogged() .catch e:', e)
                }
                return false
            },
        },

        computed: {
        },

    };
</script>

<style scoped>

</style>
