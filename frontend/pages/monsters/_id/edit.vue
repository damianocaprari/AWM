<template>
  <!--<v-container fluid>-->
  <v-container v-if="canEdit()">

    <v-row justify="center" v-if="alert || form_alert">
      <v-col cols="12" v-if="alert">
        <v-alert>{{ alert.message }}</v-alert>
      </v-col>
      <v-col cols="12" v-if="form_alert">
        <v-alert :type="form_alert.type">{{ form_alert.message }}</v-alert>
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <v-card-text>
          <v-form @submit.prevent="submit">

            <v-row>
              <v-col cols="12" sm="8">
                <v-row>
                  <v-text-field class="title" label="Name *" v-model="form_data.name" :rules="rules.required"/>
                </v-row>
                <v-row>
                  <v-col cols="12" sm="6">
                    <v-select label="Size *" :items="sizeList" v-model="form_data.size"
                              :rules="rules.required"/>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-select v-model="form_data.alignment" :items="alignmentList" :rules="rules.required"
                              label="Alignment *"></v-select>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" sm="6">
                    <v-text-field label="Type *" v-model="form_data.type" :rules="rules.required"/>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field v-if="form_data.type" label="Subtype" v-model="form_data.subtype"/>
                  </v-col>
                </v-row>

                <v-row>
                  <v-col cols="12" sm="6">
                    <v-text-field v-model="form_data.hit_point" :rules="rules.required" type="number"
                                  label="Hit points *"/>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-select v-model="form_data.hit_dice" :rules="rules.required" :items="hitDiceList"
                              label="Hit Dice *"/>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" sm="6">
                    <v-text-field type="number" label="Armor class *" v-model="form_data.armor_class"
                                  :rules="rules.required"/>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field label="Armor class Notes" v-model="form_data.armor_class_notes"/>
                  </v-col>
                </v-row>
              </v-col>

              <v-col cols="12" sm="4">
                <v-card outlined elevation="1">
                  <v-col>
                    <v-row justify="center">
                      <v-col align="center">
                        <v-avatar color="grey" tile size="160" class="mx-auto">
                          <v-img :src="monster.image"
                                 v-if="(monster.image)"></v-img>
                        </v-avatar>
                      </v-col>
                    </v-row>

                    <v-row>
                      <v-col>
                        <v-text-field v-model="monster.ability_str" type="number" label="STR *"
                                      :rules="rules.required"></v-text-field>
                        <v-text-field v-model="monster.ability_dex" type="number" label="DEX *"
                                      :rules="rules.required"></v-text-field>
                        <v-text-field v-model="monster.ability_con" type="number" label="CON *"
                                      :rules="rules.required"></v-text-field>
                      </v-col>
                      <v-col>
                        <v-text-field v-model="monster.ability_int" type="number" label="INT *"
                                      :rules="rules.required"></v-text-field>
                        <v-text-field v-model="monster.ability_wis" type="number" label="WIS *"
                                      :rules="rules.required"></v-text-field>
                        <v-text-field v-model="monster.ability_cha" type="number" label="CHA *"
                                      :rules="rules.required"></v-text-field>
                      </v-col>
                    </v-row>
                  </v-col>
                </v-card>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" sm="3">
                <v-select v-model="form_data.challenge_rating" :items="CRList" label="Challenge rating *"
                          :rules="rules.required"/>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" sm="4">
                <v-text-field v-model="form_data.speeds" label="Speeds"/>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field v-model="form_data.senses" label="Senses"/>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field v-model="form_data.languages" label="Languages"/>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <v-text-field v-model="form_data.skills" label="Skills"/>
              </v-col>
              <v-col>
                <v-text-field v-model="form_data.saves" label="Saves"/>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" lg="3">
                <v-text-field v-model="form_data.damage_vulnerabilities" label="Damage Vulnerabilities"/>
              </v-col>
              <v-col cols="12" lg="3">
                <v-text-field v-model="form_data.damage_resistances" label="Damage Resistances"/>
              </v-col>
              <v-col cols="12" lg="3">
                <v-text-field v-model="form_data.condition_immunities" label="Condition Immunities"/>
              </v-col>
              <v-col cols="12" lg="3">
                <v-text-field v-model="form_data.damage_immunities" label="Damage Immunities"/>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" sm="6">
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-textarea
                        filled
                        auto-grow
                        v-on="on"
                        label="Traits"
                        v-model="form_data.traits"
                    />
                  </template>
                  <span>Put < br > to make a new line.</span>
                </v-tooltip>
              </v-col>

              <v-col cols="12" sm="6">
                <v-tooltip top>
                  <template v-slot:activator="{ on }">

                    <v-textarea
                        filled
                        auto-grow
                        v-on="on"
                        label="Actions"
                        v-model="form_data.actions"
                    />
                  </template>
                  <span>Put < br > to make a new line.</span>
                </v-tooltip>
              </v-col>
            </v-row>


            <v-row>
              <v-col cols="12" sm="6">
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-textarea
                        filled
                        auto-grow
                        v-on="on"
                        label="Special abilities"
                        v-model="form_data.special_abilities"
                    />
                  </template>
                  <span>Put < br > to make a new line.</span>
                </v-tooltip>
              </v-col>

              <v-col cols="12" sm="6">
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-textarea
                        filled
                        auto-grow
                        v-on="on"
                        label="Legendary Actions"
                        v-model="form_data.legendary_actions"
                    />
                  </template>
                  <span>Put < br > to make a new line.</span>
                </v-tooltip>
              </v-col>
            </v-row>


            <v-row justify="center">
              <v-col class="text-center">
                <v-btn type="submit" :loading="loading" :disabled="loading" outlined color="accent">Save</v-btn>
                <v-btn text color="accent" @click="resetFormData">Cancel</v-btn>
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>


      </v-col>
    </v-row>


  </v-container>
</template>

<script>
    import api from '~/api'

    import FormData from 'form-data'

    export default {
        head() {
            return {
                title: `AWM Project - Edit ${this.monster.name}`
            };
        },
        async asyncData({$axios, params}) {
            try {
                let monster = await $axios.$get(`/monsters/${params.id}`);

                if (!monster || monster.id != params.id) {
                    return {
                        alert: {
                            type: 'error',
                            message: 'Selected monster does not exist'
                        }
                    }
                }

                let form_data = {
                    name: monster.name,
                    //image: monster.image,
                    size: monster.size,

                    type: monster.type,
                    subtype: monster.subtype,
                    alignment: monster.alignment,
                    armor_class: monster.armor_class,
                    armor_class_notes: monster.armor_class_notes,

                    hit_point: monster.hit_point,
                    hit_dice: monster.hit_dice,
                    ability_str: monster.ability_str,
                    ability_dex: monster.ability_dex,
                    ability_con: monster.ability_con,
                    ability_int: monster.ability_int,
                    ability_wis: monster.ability_wis,
                    ability_cha: monster.ability_cha,
                    challenge_rating: monster.challenge_rating,

                    traits: monster.traits,
                    speeds: monster.speeds,
                    saves: monster.saves,
                    skills: monster.skills,
                    damage_vulnerabilities: monster.damage_vulnerabilities,
                    damage_resistances: monster.damage_resistances,
                    condition_immunities: monster.condition_immunities,
                    damage_immunities: monster.damage_immunities,
                    senses: monster.senses,
                    languages: monster.languages,
                    special_abilities: monster.special_abilities,
                    actions: monster.actions,
                    legendary_actions: monster.legendary_actions,

                };

                return {monster, form_data};
            } catch (e) {
                return {monster: []};
            }
        },
        data() {
            return {
                monster: {},
                loading: false,
                rules: {
                    required: [
                        v => !!v || 'Field is required'
                    ],
                },
                form_alert: null,
                alert: null,


                form_data: {
                    name: '',
                    //image: '',
                    size: '',

                    type: '',
                    subtype: '',
                    alignment: '',
                    armor_class: '',
                    armor_class_notes: '',

                    hit_point: '',
                    hit_dice: '',
                    ability_str: '',
                    ability_dex: '',
                    ability_con: '',
                    ability_int: '',
                    ability_wis: '',
                    ability_cha: '',
                    challenge_rating: '',

                    traits: '',
                    speeds: '',
                    saves: '',
                    skills: '',
                    damage_vulnerabilities: '',
                    damage_resistances: '',
                    condition_immunities: '',
                    damage_immunities: '',
                    senses: '',
                    languages: '',
                    special_abilities: '',
                    actions: '',
                    legendary_actions: '',
                },

                alert: null,
                isEditing: true,

                CRList: [
                    {text: "All", value: null},
                    {text: "1/8", value: "1/8"},
                    {text: "1/4", value: "1/4"},
                    {text: "1/2", value: "1/2"},
                    {text: "1", value: "1"},
                    {text: "2", value: "2"},
                    {text: "3", value: "3"},
                    {text: "4", value: "4"},
                    {text: "5", value: "5"},
                    {text: "6", value: "6"},
                    {text: "7", value: "7"},
                    {text: "8", value: "8"},
                    {text: "9", value: "9"},
                    {text: "10", value: "10"},
                    {text: "11", value: "11"},
                    {text: "12", value: "12"},
                    {text: "13", value: "13"},
                    {text: "14", value: "14"},
                    {text: "15", value: "15"},
                    {text: "16", value: "16"},
                    {text: "17", value: "17"},
                    {text: "18", value: "18"},
                    {text: "19", value: "19"},
                    {text: "20", value: "20"},
                ],
                sizeList: [
                    {text: "Fine", value: "Fine"},
                    {text: "Diminutive", value: "Diminutive"},
                    {text: "Tiny", value: "Tiny"},
                    {text: "Small", value: "Small"},
                    {text: "Medium", value: "Medium"},
                    {text: "Large", value: "Large"},
                    {text: "Huge", value: "Huge"},
                    {text: "Gargantuan", value: "Gargantuan"},
                    {text: "Colossal", value: "Colossal"},
                ],
                alignmentList: [
                    {text: 'Lawful Good', value: 'Lawful Good'},
                    {text: 'Neutral Good', value: 'Neutral Good'},
                    {text: 'Chaotic Good', value: 'Chaotic Good'},
                    {text: 'Lawful Neutral', value: 'Lawful Neutral'},
                    {text: 'True Neutral', value: 'True Neutral'},
                    {text: 'Chaotic Neutral', value: 'Chaotic Neutral'},
                    {text: 'Lawful Evil', value: 'Lawful Evil'},
                    {text: 'Neutral Evil', value: 'Neutral Evil'},
                    {text: 'Chaotic Evil', value: 'Chaotic Evil'},
                ],
                hitDiceList: [
                    {text: '1d3', value: '1d3'},
                    {text: '1d4', value: '1d4'},
                    {text: '1d6', value: '1d6'},
                    {text: '1d8', value: '1d8'},
                    {text: '1d10', value: '1d10'},
                    {text: '1d12', value: '1d12'},
                ]
            };
        },
        methods: {
            resetFormData() {
                this.form_data = {
                    name: this.monster.name,
                    //image: this.monster.image,
                    size: this.monster.size,

                    type: this.monster.type,
                    subtype: this.form_data.subtype,
                    alignment: this.form_data.alignment,
                    armor_class: this.form_data.armor_class,
                    armor_class_notes: this.form_data.armor_class_notes,

                    hit_point: this.form_data.hit_point,
                    hit_dice: this.form_data.hit_dice,
                    ability_str: this.form_data.ability_str,
                    ability_dex: this.form_data.ability_dex,
                    ability_con: this.form_data.ability_con,
                    ability_int: this.form_data.ability_int,
                    ability_wis: this.form_data.ability_wis,
                    ability_cha: this.form_data.ability_cha,
                    challenge_rating: this.form_data.challenge_rating,

                    traits: this.form_data.traits,
                    speeds: this.form_data.speeds,
                    saves: this.form_data.saves,
                    skills: this.form_data.skills,
                    damage_vulnerabilities: this.form_data.damage_vulnerabilities,
                    damage_resistances: this.form_data.damage_resistances,
                    condition_immunities: this.form_data.condition_immunities,
                    damage_immunities: this.form_data.damage_immunities,
                    senses: this.form_data.senses,
                    languages: this.form_data.languages,
                    special_abilities: this.form_data.special_abilities,
                    actions: this.form_data.actions,
                    legendary_actions: this.form_data.legendary_actions,

                }
                this.$router.push(`/monsters/${this.$route.params.id}`)

            },

            submitSBAGLIATA() {
                let editedMonster = this.monster
                //console.log(editedMonster.image)
                //if (editedMonster.image.indexOf("http://") != -1) {
                //    delete editedMonster["image"]
                //}
                const config = {
                    headers: {"content-type": "multipart/form-data"}
                };
                let formData = new FormData();
                for (let data in editedMonster) {
                    formData.append(data, editedMonster[data]);
                }
                try {
                    let response = this.$axios.$put(`/monsters/${editedMonster.id}/`, formData, config);
                    //this.$router.push("/monsters/");
                    this.$router.push(`/monsters/${this.$route.params.id}`)
                } catch (e) {
                    console.log(e);
                }

            },


            submit() {
                //console.log(this.form_data)
                //if (this.isEditing == false) return
                this.alert = null
                this.loading = true
                api.updateMonster(this.$axios, this.monster.id, this.form_data)
                    .then(result => {
                        console.log('/account/edit.vue .then() result', result)
                        this.alert = {type: 'success', message: result.message || 'Success'}
                        this.loading = false
                        this.isEditing = false

                        this.monster.name = this.form_data.name
                        //this.monster.image = this.form_data.image
                        this.monster.size = this.form_data.size

                        this.monster.type = this.form_data.type
                        this.monster.subtype = this.form_data.subtype
                        this.monster.alignment = this.form_data.alignment
                        this.monster.armor_class = this.form_data.armor_class
                        this.monster.armor_class_notes = this.form_data.armor_class_notes

                        this.monster.hit_point = this.form_data.hit_point
                        this.monster.hit_dice = this.form_data.hit_dice
                        this.monster.ability_str = this.form_data.ability_str
                        this.monster.ability_dex = this.form_data.ability_dex
                        this.monster.ability_con = this.form_data.ability_con
                        this.monster.ability_int = this.form_data.ability_int
                        this.monster.ability_wis = this.form_data.ability_wis
                        this.monster.ability_cha = this.form_data.ability_cha
                        this.monster.challenge_rating = this.form_data.challenge_rating

                        this.monster.traits = this.form_data.traits
                        this.monster.speeds = this.form_data.speeds
                        this.monster.saves = this.form_data.saves
                        this.monster.skills = this.form_data.skills
                        this.monster.damage_vulnerabilities = this.form_data.damage_vulnerabilities
                        this.monster.damage_resistances = this.form_data.damage_resistances
                        this.monster.condition_immunities = this.form_data.condition_immunities
                        this.monster.damage_immunities = this.form_data.damage_immunities
                        this.monster.senses = this.form_data.senses
                        this.monster.languages = this.form_data.languages
                        this.monster.special_abilities = this.form_data.special_abilities
                        this.monster.actions = this.form_data.actions
                        this.monster.legendary_actions = this.form_data.legendary_actions

                        //this.user.last_name = this.form_data.last_name
                        //this.user.email = this.form_data.email
                        this.$router.push('/monsters')
                    })
                    .catch(error => {

                        console.log('/monsters/add.vue $axios->monster ERROR:', error.response || error)
                        if (error.response && error.response.data) {
                            this.form_alert = {
                                type: 'error',
                                message: this.handleErrorMsg(error.response.data)
                            }

                        }
                        this.loading = false

                        /*
                        console.log('/account/edit.vue .catch() error', error)
                        console.log('/account/edit.vue .catch() error.response', error.response)
                        this.loading = false
                        if (error.response && error.response.data) {
                            this.alert = {
                                type: 'error',
                                message: error.response.data || 'Error'
                            }
                        }*/
                    })
                //this.$router.push('/monsters')

            },

            handleErrorMsg(data) {
                if (data.name) return `Error with "name": ${data.name[0]}`
                if (data.alignment) return `Error with "alignment": ${data.alignment[0]}`
                if (data.challenge_rating) return `Error with "challenge_rating": ${data.challenge_rating[0]}`
                if (data.hit_point) return `Error with "hit_point": ${data.hit_point[0]}`
                if (data.hit_dice) return `Error with "hit_dice": ${data.hit_dice[0]}`
                if (data.armor_class) return `Error with "armor_class": ${data.armor_class[0]}`
                if (data.size) return `Error with "size": ${data.size[0]}`
                if (data.type) return `Error with "type": ${data.type[0]}`
                //if (data.image) return `Error with "image: ${data.image[0]}`
                if (data.ability_str) return `Error with "ability_str": ${data.ability_str[0]}`
                if (data.ability_dex) return `Error with "ability_dex": ${data.ability_dex[0]}`
                if (data.ability_con) return `Error with "ability_con: ${data.ability_con[0]}`
                if (data.ability_int) return `Error with "ability_int": ${data.ability_int[0]}`
                if (data.ability_wis) return `Error with "ability_wis": ${data.ability_wis[0]}`
                if (data.ability_cha) return `Error with "ability_cha: ${data.ability_cha[0]}`
                return `Error`
            },

            onDelete(id) {
                console.log(id)
            },

            canEdit() {
                try {
                    let userId = this.$store.state.auth.user.id
                    if (this.monster && this.monster.author) {
                        let monsterAuthorId = this.$store.app.getResourceId(this.monster.author)
                        if (userId == monsterAuthorId)
                            return true
                    }
                } catch (e) {
                    console.log('monsters/_id/edit.vue canEdit() .catch e:', e)
                }
                this.$router.push('/')
            },


            //------------------
            //------------------
            onFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length) {
                    return;
                }
                this.monster.image = files[0];
                this.createImage(files[0]);
            },
            createImage(file) {
                // let image = new Image();
                let reader = new FileReader();
                let vm = this;
                reader.onload = e => {
                    vm.preview = e.target.result;
                };
                reader.readAsDataURL(file);
            },

        }
    };

</script>

<style scoped>
  .boldedname {
    font-weight: bold
  }

  span {
    margin-right: 3px
  }

  .subtitle {
    font-size: 30px;
    font-weight: bold;
  }

</style>
