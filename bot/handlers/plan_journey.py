from telegram import Update
from telegram.ext import ContextTypes
from bot.services.tfl_api import journey_planner

async def plan_journey_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	user = update.effective_user
	args = context.args

	if len(args) < 2:
		await update.message.reply_text(
			f"Hi {user.first_name or 'there'}! 👋\n"
			"Please provide both a starting location and a destination.\n"
			"Usage: /plan_journey <from_location> <to_location>"
		)
		return

	from_loc = args[0]
	to_loc = args[1]

	journey_info = journey_planner(from_loc, to_loc)

	await update.message.reply_text(
		f"Hi {user.first_name or 'there'}! 👋\n"
		f"{journey_info}"
	)