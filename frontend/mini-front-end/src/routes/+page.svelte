<script>
	let username = '';
	let password = '';
	let isSuccess = false;
	async function login() {
		const res = await fetch('http://127.0.0.1:8000/auth', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				username: username,
				password: password
			})
		});

		const json = await res.json();
		let result = JSON.stringify(json);
		if (json['status'] == 'User Successfully Login!') {
			isSuccess = true;
		}
	}
</script>

<section class="flex h-screen w-screen justify-center items-center bg-[#FFEFD6]">
	<div class="flex flex-col w-[500px] p-10 shadow-md bg-white rounded-md space-y-4">
		{#if isSuccess}
			<p class="text-4xl font-bold text-green-400 text-center mb-8">Success</p>
		{:else}
			<p class="text-4xl font-bold text-green-400 text-center mb-8">Log In</p>
		{/if}

		<div>
			<input
				bind:value={username}
				type="text"
				class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
				placeholder="User Name"
				required
			/>
		</div>
		<div>
			<input
				bind:value={password}
				type="text"
				class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
				placeholder="Password"
				required
			/>
		</div>
		<button
			on:click={login}
			class="bg-green-400 py-3 rounded-md text-white font-bold hover:bg-green-500 hover:shadow-md hover:shadow-green-400"
			>Button</button
		>
	</div>
</section>
