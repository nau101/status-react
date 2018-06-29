(ns status-im.data-store.realm.schemas.account.v8.transport)

(def schema {:name       :transport
             :primaryKey :chat-id
             :properties {:chat-id               :string
                          :ack                   :string
                          :seen                  :string
                          :pending-ack           :string
                          :pending-send          :string
                          :topic                 :string
                          :one-to-one            {:type    :bool
                                                  :optional true}
                          :fetch-history?        {:type    :bool
                                                  :default false}
                          :resend?               {:type     :string
                                                  :optional true}
                          :sym-key-id            {:type    :string
                                                  :optional true}
                          ;;TODO (yenda) remove once go implements persistence
                          :sym-key               {:type     :string
                                                  :optional true}}})
