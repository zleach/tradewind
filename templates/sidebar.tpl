<br>
<div class="panel panel-default">
    <div class="panel-heading">
        <h3>Tradewind</h3>
        <p>Ship's company generator<br><span class="text-muted">by u/mercuryvii</span></p>        
    </div>
    <div class="panel-body">
        <!-- Theme Toggle -->
        <div class="theme-toggle-label">
            <span>Theme</span>
            <button type="button" class="theme-toggle" id="themeToggle" aria-label="Toggle theme (Auto/Light/Dark)" title="Auto (follows system)"></button>
        </div>
        
        <form role="form">
            <div class="form-group">
                <label for="prefixInput">Prefix</label>
                <input type="text" class="form-control" id="prefixInput" name="prefix" placeholder="USS, UNSC, HMS" value="{{ prefix }}">
            </div>
            <div class="form-group">
                <label for="crewSizeSelect">Crew Size</label>
                <select class="form-control input-sm" id="crewSizeSelect" name="crewSize">
                    {% set sizes = ['Tiny','Small','Normal','Large','Extra-Large'] %}
                    {% set index = 1 %}
                    {% for size in sizes %}
                        <option value="{{ index }}"
                        {% if crewSize == index %}
                            selected = "selected"
                        {% endif %}
                        >{{ size }}</option>
                        {% set index = index + 1 %}
                    {% endfor %}
                </select>
            </div>
            <div class="form-group">
                <label for="shipSelect">Class</label>
                <select class="form-control input-sm" name="type">
                    <option value="0">Random</option>
                    {% set index = 1 %}
                    {% for type in types %}
                        <option value="{{ index }}"
                        {% if shipType == index %}
                            selected = "selected"
                        {% endif %}
                        >{{ type['name'] }} ({{ type['designation'] }})</option>
                        {% set index = index + 1 %}
                    {% endfor %}
                </select>
            </div>
            <button type="submit" class="btn btn-success">Generate New Ship</button>
        </form>
    </div>
</div>
