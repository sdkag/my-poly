const FETCH_ALL_QUESTIONS = "questions/FETCH_ALL_QUESTIONS";
const REMOVE_USER = "session/REMOVE_USER";

const loadQuestions = (questions) => ({
    type: FETCH_ALL_QUESTIONS,
    payload: questions
})



export const fetchAllQuestions = () => async (dispatch) => fetch('api/questions')
	  .then(res=> res.json())
		.then(({questions}) => dispatch(loadQuestions(questions)))


const initialState = {
	byId: null,
	allIds: null
}
export default (state=initialState, action) => {
	switch (action.type){
		case FETCH_ALL_QUESTIONS:
			const byIds = {}
			const allIds = []
			for (const q in action.questions) {
				byIds[q.id] = q
				allIds.push(q.id)
			}
			return {...state, byIds, allIds }
		default:
			return state;
	}
}