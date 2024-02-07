export const Input_Form= () => {
    return (
        <>
            <h2>Fill out the following form to test against model!!!</h2>
            <form action="http://localhost/5000/api/get_result" method="GET">
                <h4>Select a Planet</h4>
                <select id = "homeworld" name = 'homeworld'>
                <option value="Tatooine">Tatooine</option>
                <option value="Alderaan">Alderaan</option>
                <option value="Sullust">Sullust</option>
                <option value="Iktotch">Iktotch</option>
                <option value="Dagobah">Dagobah</option>
                <option value="Tholoth">Tholoth</option>
                </select>


                <h4>Select a Unit Type</h4>
                <select id = "unit_type" name = 'unit_type'>
                <option value="stormtrooper">Stormtrooper</option>
                <option value="tie_silencer">Tie Silencer</option>
                <option value="resistance_soldier">Resistance Soldier</option>
                <option value="x-wing">X-Wing</option>
                <option value="at-st">At-St</option>
                <option value="at-at">at-at</option>
                </select>

                <input type="submit"></input>
            </form>

        </>
    );
}