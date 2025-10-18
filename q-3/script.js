// 1. Find the hidden text box by its unique ID
var textBox = document.querySelector('#q-generate-addresses-with-llms');

// 2. Force it to become visible by overriding its CSS
textBox.style.display = 'block';

// 3. Force it to be enabled
textBox.disabled = false;

// 4. Assign JSON string with correct schema - Modify the schema as given in your question
textBox.value = '{"model":"gpt-4o-mini","messages":[{"role":"system","content":"Respond in JSON"},{"role":"user","content":"Generate 10 random addresses in the US"}],"response_format":{"type":"json_schema","json_schema":{"name":"addresses_schema","strict":true,"schema":{"type":"object","properties":{"addresses":{"type":"array","items":{"type":"object","properties":{"county":{"type":"string"},"apartment":{"type":"string"},"zip":{"type":"number"}},"required":["county","apartment","zip"],"additionalProperties":false}}},"required":["addresses"],"additionalProperties":false}}}}';

// 5. Trigger input event
textBox.dispatchEvent(new Event('input',{ bubbles:true }));
console.log("SUCCESS! JSON string is now correctly assigned.");

// Verify by check button