{% macro render_person(person) -%}
{{ person.personality }} {{ person.age }}-year-old {{ person.genderPronoun }} has {{ person.eyecolor }} eyes, a {{ person.skincolor }} complexion, and {{ person.hairtype }} {{ person.haircolor }} hair {{ person.hairstyle }}.
{{ person.genderTitle|capitalize }} is {{ person.height }} and {{ person.build }}. {{ person.genderTitle|capitalize }} is from  {{ person.birthPlace }}.
{% if person.previousService %}
    {{ person.rank.title }} {{ person.lastName }} previously served aboard the {{ prefix }} {{ person.previousService }}.
{% endif %}
{%- endmacro %}

<div class="container">
    <div class="row">
        <div class="col-md-9">
            <h1 class="">{{ ship.prefix }} {{ ship.name }}</h1>
            <h3 class="">{{ ship.typeName }} ({{ship.typeCode}}-{{ship.idNumber}})</h3>

            <div class="row">
                {% if ship.hasCommandElement %}
                <div class="col-md-7">            
                    <h5>Command</h5>
                    <strong>{{ ship.co.rank.title }} {{ ship.co }}, Commanding Officer</strong>
                    <p>{{ ship.co.rank.title }} {{ ship.co.lastName }} is a 
                    {{ render_person(ship.co) }}
                        {{ ship.co.genderPossessive|capitalize }} executive officer is {{ ship.xo.rank.title }} {{ ship.xo }}.
                    </p>
                </div>
                {% endif %}
                <div class="col-md-5">
                    <h5>General Characteristics</h5>
                    <table class="table table-condensed characteristics">
                        <tr>
                            <td>Status:</td>
                            <td>Active service as of {{ ship.activeServiceDate.strftime("%Y") }}</td>
                        </tr>
                        <tr>
                            <td>Commissioned:</td>
                            <td>{{ ship.commissionedDate.strftime("%B %d, %Y") }}</td>
                        </tr>
                        <tr>
                            <td>Homeport:</td>
                            <td>{{ ship.homeport }}</td>
                        </tr>

                    </table>
                </div>
            </div>
            <hr>
            {% for division in ship.divisions %}
                <h5>{{ division.name }}</h5>
                <table class="table table-striped table-bordered">
                    {% for person in division.crew %}
                        <tr>
                            <td><abbr title="{{ person.rank.title }}">{{ person.rank.abbrivation }}</abbr></td>
                            <td class="name">
                                <strong>{{ person }}</strong>
                                <br>This
                                    {{ render_person(person) }}                   
                            </td>
                            <td>{{ person.rank.title }}</td>
                            <td>{{ person.gender.capitalize() }}</td>
                        </tr>
                {% endfor %}
                </table>
            {% endfor %}
        </div>
        <div class="col-md-3">
            {% include('sidebar.tpl') %}
        </div>

    </div>
</div>