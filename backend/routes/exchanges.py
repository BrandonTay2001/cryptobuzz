from flask import Blueprint, jsonify, request
from util.exchange_util import ExchangeUtil

exchanges_bp = Blueprint('exchanges', __name__)

@exchanges_bp.route('/getExchanges')
def get_exchanges():
    ticker = request.args.get('ticker')

    exchange_util = ExchangeUtil()
    exchanges = exchange_util.get_exchanges_for_ticker(ticker)
    return jsonify({
        'status': 'success',
        'data': exchanges
    }), 200