from typing import List, Any, Optional
import datetime

from .models import _BaseModel
from .enums import _PrintableEnum


class Root(_BaseModel):
    class Relations(_PrintableEnum):
        class releases:
            """
            Type: Release[]
            """

            value = "releases"

        class accountOnboardingSteps:
            """
            Type: AccountOnboardingStep[]
            """

            value = "accountOnboardingSteps"

        class account:
            """
            Type: Account
            """

            value = "account"

        class loggedInUser:
            """
            Type: User
            """

            value = "loggedInUser"

        class cardsStatusHistory:
            """
            Type: CardsStatusHistory[]
            """

            value = "cardsStatusHistory"

        class cardsEffortHistory:
            """
            Type: CardsEffortHistory[]
            """

            value = "cardsEffortHistory"

        class cardsFinishedHistory:
            """
            Type: CardsFinishedHistory[]
            """

            value = "cardsFinishedHistory"

        class cardsTimeToFinished:
            """
            Type: CardsTimeToFinished[]
            """

            value = "cardsTimeToFinished"

    releases: List["Release"]
    accountOnboardingSteps: List["AccountOnboardingStep"]
    account: "Account"
    loggedInUser: "User"
    cardsStatusHistory: List["CardsStatusHistory"]
    cardsEffortHistory: List["CardsEffortHistory"]
    cardsFinishedHistory: List["CardsFinishedHistory"]
    cardsTimeToFinished: List["CardsTimeToFinished"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountOnboardingStep(_BaseModel):
    class Fields(_PrintableEnum):
        class chapter:
            """
            Type: str
            """

            value = "chapter"

        class description:
            """
            Type: str
            """

            value = "description"

        class milestone:
            """
            Type: str
            """

            value = "milestone"

        class sortValue:
            """
            Type: str
            """

            value = "sortValue"

        class title:
            """
            Type: str
            """

            value = "title"

        class variants:
            """
            Type: list
            """

            value = "variants"

        class xp:
            """
            Type: int
            """

            value = "xp"

    chapter: str
    description: str
    milestone: str
    sortValue: str
    title: str
    variants: list
    xp: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountOnboarding(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class steps:
            """
            Type: str
            """

            value = "steps"

        class variants:
            """
            Type: list
            """

            value = "variants"

    account: "Account"
    steps: str
    variants: list

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountRole(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class isBillingContact:
            """
            Type: str
            """

            value = "isBillingContact"

        class lastChangedAt:
            """
            Type: datetime.datetime
            """

            value = "lastChangedAt"

        class role:
            """
            Type: str
            """

            value = "role"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    createdAt: datetime.datetime
    isBillingContact: str
    lastChangedAt: datetime.datetime
    role: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountSetting(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class key:
            """
            Type: str
            """

            value = "key"

        class usesDefault:
            """
            Type: str
            """

            value = "usesDefault"

        class value:
            """
            Type: str
            """

            value = "value"

    account: "Account"
    key: str
    usesDefault: str
    value: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountUserAchievement(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class context:
            """
            Type: str
            """

            value = "context"

        class user:
            """
            Type: User
            """

            value = "user"

        class value:
            """
            Type: str
            """

            value = "value"

    account: "Account"
    context: str
    user: "User"
    value: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountUserSetting(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class inboxDeck:
            """
            Type: Deck
            """

            value = "inboxDeck"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    inboxDeck: "Deck"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Account(_BaseModel):
    class Fields(_PrintableEnum):
        class activeFeatureFlags:
            """
            Type: str
            """

            value = "activeFeatureFlags"

        class activeProjectCount:
            """
            Type: int
            """

            value = "activeProjectCount"

        class allowInheritHeroCover:
            """
            Type: bool
            """

            value = "allowInheritHeroCover"

        class attachmentCoverMode:
            """
            Type: str
            """

            value = "attachmentCoverMode"

        class billingCity:
            """
            Type: str
            """

            value = "billingCity"

        class billingCountryCode:
            """
            Type: str
            """

            value = "billingCountryCode"

        class billingLine1:
            """
            Type: str
            """

            value = "billingLine1"

        class billingLine2:
            """
            Type: str
            """

            value = "billingLine2"

        class billingName:
            """
            Type: str
            """

            value = "billingName"

        class billingType:
            """
            Type: str
            """

            value = "billingType"

        class billingZip:
            """
            Type: str
            """

            value = "billingZip"

        class coupon:
            """
            Type: str
            """

            value = "coupon"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class dependenciesEnabled:
            """
            Type: bool
            """

            value = "dependenciesEnabled"

        class disabledAt:
            """
            Type: datetime.datetime
            """

            value = "disabledAt"

        class disabledBy:
            """
            Type: User
            """

            value = "disabledBy"

        class effortScale:
            """
            Type: str
            """

            value = "effortScale"

        class hideCompletedCardCountForDecks:
            """
            Type: bool
            """

            value = "hideCompletedCardCountForDecks"

        class id:
            """
            Type: str
            """

            value = "id"

        class isDisabled:
            """
            Type: bool
            """

            value = "isDisabled"

        class isLearning:
            """
            Type: bool
            """

            value = "isLearning"

        class isNonProfit:
            """
            Type: bool
            """

            value = "isNonProfit"

        class maxHandSlotCount:
            """
            Type: int
            """

            value = "maxHandSlotCount"

        class maxTimeTrackingSegmentMsDuration:
            """
            Type: int
            """

            value = "maxTimeTrackingSegmentMsDuration"

        class milestonesEnabled:
            """
            Type: bool
            """

            value = "milestonesEnabled"

        class name:
            """
            Type: str
            """

            value = "name"

        class netGiftAmount:
            """
            Type: str
            """

            value = "netGiftAmount"

        class offeringTrial:
            """
            Type: bool
            """

            value = "offeringTrial"

        class persona:
            """
            Type: str
            """

            value = "persona"

        class priorityLabels:
            """
            Type: str
            """

            value = "priorityLabels"

        class seats:
            """
            Type: int
            """

            value = "seats"

        class staffPermission:
            """
            Type: str
            """

            value = "staffPermission"

        class statusChangeDurations:
            """
            Type: str
            """

            value = "statusChangeDurations"

        class subdomain:
            """
            Type: str
            """

            value = "subdomain"

        class timeTrackingMode:
            """
            Type: str
            """

            value = "timeTrackingMode"

        class timeTrackingSwimLaneInfo:
            """
            Type: bool
            """

            value = "timeTrackingSwimLaneInfo"

        class totalMediaByteUsage:
            """
            Type: int
            """

            value = "totalMediaByteUsage"

        class workdays:
            """
            Type: str
            """

            value = "workdays"

        class workflowMode:
            """
            Type: str
            """

            value = "workflowMode"

    class Relations(_PrintableEnum):
        class cards:
            """
            Type: Card[]
            """

            value = "cards"

        class invoices:
            """
            Type: Invoice[]
            """

            value = "invoices"

        class cardPresets:
            """
            Type: CardPreset[]
            """

            value = "cardPresets"

        class attachments:
            """
            Type: Attachment[]
            """

            value = "attachments"

        class discordGuilds:
            """
            Type: DiscordGuild[]
            """

            value = "discordGuilds"

        class timeTrackingSegments:
            """
            Type: TimeTrackingSegment[]
            """

            value = "timeTrackingSegments"

        class workflowItems:
            """
            Type: WorkflowItem[]
            """

            value = "workflowItems"

        class deckAssignments:
            """
            Type: DeckAssignment[]
            """

            value = "deckAssignments"

        class assigneeAssignments:
            """
            Type: AssigneeAssignment[]
            """

            value = "assigneeAssignments"

        class assigneeDeckAssignments:
            """
            Type: AssigneeDeckAssignment[]
            """

            value = "assigneeDeckAssignments"

        class wizards:
            """
            Type: Wizard[]
            """

            value = "wizards"

        class milestones:
            """
            Type: Milestone[]
            """

            value = "milestones"

        class handCards:
            """
            Type: HandCard[]
            """

            value = "handCards"

        class resolvables:
            """
            Type: Resolvable[]
            """

            value = "resolvables"

        class cardUpvotes:
            """
            Type: CardUpvote[]
            """

            value = "cardUpvotes"

        class resolvableParticipants:
            """
            Type: ResolvableParticipant[]
            """

            value = "resolvableParticipants"

        class userReportSettings:
            """
            Type: UserReportSetting[]
            """

            value = "userReportSettings"

        class cardOrders:
            """
            Type: CardOrder[]
            """

            value = "cardOrders"

        class accountUserAchievements:
            """
            Type: AccountUserAchievement[]
            """

            value = "accountUserAchievements"

        class userInviteCodes:
            """
            Type: UserInviteCode[]
            """

            value = "userInviteCodes"

        class decks:
            """
            Type: Deck[]
            """

            value = "decks"

        class queueEntries:
            """
            Type: QueueEntry[]
            """

            value = "queueEntries"

        class anyDecks:
            """
            Type: Deck[]
            """

            value = "anyDecks"

        class projects:
            """
            Type: Project[]
            """

            value = "projects"

        class archivedProjects:
            """
            Type: Project[]
            """

            value = "archivedProjects"

        class anyProjects:
            """
            Type: Project[]
            """

            value = "anyProjects"

        class onboardingDeck:
            """
            Type: Deck
            """

            value = "onboardingDeck"

        class deckSubscriptions:
            """
            Type: DeckSubscription[]
            """

            value = "deckSubscriptions"

        class roles:
            """
            Type: AccountRole[]
            """

            value = "roles"

        class invitations:
            """
            Type: UserInvitation[]
            """

            value = "invitations"

        class githubIntegration:
            """
            Type: Integration
            """

            value = "githubIntegration"

        class slackIntegration:
            """
            Type: Integration
            """

            value = "slackIntegration"

        class affiliateCodes:
            """
            Type: AffiliateCode[]
            """

            value = "affiliateCodes"

        class activities:
            """
            Type: Activity[]
            """

            value = "activities"

        class stripeAccountSync:
            """
            Type: StripeAccountSync
            """

            value = "stripeAccountSync"

        class accountOnboarding:
            """
            Type: AccountOnboarding
            """

            value = "accountOnboarding"

    activeFeatureFlags: str
    activeProjectCount: int
    allowInheritHeroCover: bool
    attachmentCoverMode: str
    billingCity: str
    billingCountryCode: str
    billingLine1: str
    billingLine2: str
    billingName: str
    billingType: str
    billingZip: str
    coupon: str
    createdAt: datetime.datetime
    dependenciesEnabled: bool
    disabledAt: datetime.datetime
    disabledBy: "User"
    effortScale: str
    hideCompletedCardCountForDecks: bool
    id: str
    isDisabled: bool
    isLearning: bool
    isNonProfit: bool
    maxHandSlotCount: int
    maxTimeTrackingSegmentMsDuration: int
    milestonesEnabled: bool
    name: str
    netGiftAmount: str
    offeringTrial: bool
    persona: str
    priorityLabels: str
    seats: int
    staffPermission: str
    statusChangeDurations: str
    subdomain: str
    timeTrackingMode: str
    timeTrackingSwimLaneInfo: bool
    totalMediaByteUsage: int
    workdays: str
    workflowMode: str
    cards: List["Card"]
    invoices: List["Invoice"]
    cardPresets: List["CardPreset"]
    attachments: List["Attachment"]
    discordGuilds: List["DiscordGuild"]
    timeTrackingSegments: List["TimeTrackingSegment"]
    workflowItems: List["WorkflowItem"]
    deckAssignments: List["DeckAssignment"]
    assigneeAssignments: List["AssigneeAssignment"]
    assigneeDeckAssignments: List["AssigneeDeckAssignment"]
    wizards: List["Wizard"]
    milestones: List["Milestone"]
    handCards: List["HandCard"]
    resolvables: List["Resolvable"]
    cardUpvotes: List["CardUpvote"]
    resolvableParticipants: List["ResolvableParticipant"]
    userReportSettings: List["UserReportSetting"]
    cardOrders: List["CardOrder"]
    accountUserAchievements: List["AccountUserAchievement"]
    userInviteCodes: List["UserInviteCode"]
    decks: List["Deck"]
    queueEntries: List["QueueEntry"]
    anyDecks: List["Deck"]
    projects: List["Project"]
    archivedProjects: List["Project"]
    anyProjects: List["Project"]
    onboardingDeck: "Deck"
    deckSubscriptions: List["DeckSubscription"]
    roles: List["AccountRole"]
    invitations: List["UserInvitation"]
    githubIntegration: "Integration"
    slackIntegration: "Integration"
    affiliateCodes: List["AffiliateCode"]
    activities: List["Activity"]
    stripeAccountSync: "StripeAccountSync"
    accountOnboarding: "AccountOnboarding"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ActiveTimeTracker(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class card:
            """
            Type: Card
            """

            value = "card"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    card: "Card"
    createdAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Activity(_BaseModel):
    class Fields(_PrintableEnum):
        class card:
            """
            Type: Card
            """

            value = "card"

        class changer:
            """
            Type: User
            """

            value = "changer"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class data:
            """
            Type: str
            """

            value = "data"

        class deck:
            """
            Type: Deck
            """

            value = "deck"

        class isRemovedFromDeckEntry:
            """
            Type: bool
            """

            value = "isRemovedFromDeckEntry"

        class isRemovedFromMilestoneEntry:
            """
            Type: bool
            """

            value = "isRemovedFromMilestoneEntry"

        class milestone:
            """
            Type: Milestone
            """

            value = "milestone"

        class project:
            """
            Type: Project
            """

            value = "project"

        class type:
            """
            Type: str
            """

            value = "type"

    card: "Card"
    changer: "User"
    createdAt: datetime.datetime
    data: str
    deck: "Deck"
    isRemovedFromDeckEntry: bool
    isRemovedFromMilestoneEntry: bool
    milestone: "Milestone"
    project: "Project"
    type: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AffiliateCodeStat(_BaseModel):
    class Fields(_PrintableEnum):
        class affiliateCode:
            """
            Type: AffiliateCode
            """

            value = "affiliateCode"

        class month:
            """
            Type: int
            """

            value = "month"

        class newVisitors:
            """
            Type: int
            """

            value = "newVisitors"

        class revenue:
            """
            Type: int
            """

            value = "revenue"

        class signups:
            """
            Type: int
            """

            value = "signups"

        class visits:
            """
            Type: int
            """

            value = "visits"

        class year:
            """
            Type: int
            """

            value = "year"

    affiliateCode: "AffiliateCode"
    month: int
    newVisitors: int
    revenue: int
    signups: int
    visits: int
    year: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AffiliateCode(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class code:
            """
            Type: str
            """

            value = "code"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class creator:
            """
            Type: User
            """

            value = "creator"

        class isDeleted:
            """
            Type: bool
            """

            value = "isDeleted"

        class isDisabled:
            """
            Type: bool
            """

            value = "isDisabled"

        class label:
            """
            Type: str
            """

            value = "label"

        class message:
            """
            Type: str
            """

            value = "message"

        class remainingRedemptions:
            """
            Type: int
            """

            value = "remainingRedemptions"

        class reward:
            """
            Type: str
            """

            value = "reward"

        class validUntil:
            """
            Type: Any
            """

            value = "validUntil"

        class vanityUrl:
            """
            Type: str
            """

            value = "vanityUrl"

    class Relations(_PrintableEnum):
        class stats:
            """
            Type: AffiliateCodeStat[]
            """

            value = "stats"

    account: "Account"
    code: str
    createdAt: datetime.datetime
    creator: "User"
    isDeleted: bool
    isDisabled: bool
    label: str
    message: str
    remainingRedemptions: int
    reward: str
    validUntil: Any
    vanityUrl: str
    stats: List["AffiliateCodeStat"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AssigneeAssignment(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class assignedBy:
            """
            Type: User
            """

            value = "assignedBy"

        class assignee:
            """
            Type: User
            """

            value = "assignee"

        class lastAssignedAt:
            """
            Type: datetime.datetime
            """

            value = "lastAssignedAt"

    account: "Account"
    assignedBy: "User"
    assignee: "User"
    lastAssignedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AssigneeDeckAssignment(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class assignedBy:
            """
            Type: User
            """

            value = "assignedBy"

        class assignee:
            """
            Type: User
            """

            value = "assignee"

        class deck:
            """
            Type: Deck
            """

            value = "deck"

        class lastAssignedAt:
            """
            Type: datetime.datetime
            """

            value = "lastAssignedAt"

    account: "Account"
    assignedBy: "User"
    assignee: "User"
    deck: "Deck"
    lastAssignedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Attachment(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class card:
            """
            Type: Card
            """

            value = "card"

        class content:
            """
            Type: str
            """

            value = "content"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class creator:
            """
            Type: User
            """

            value = "creator"

        class file:
            """
            Type: File
            """

            value = "file"

        class title:
            """
            Type: str
            """

            value = "title"

    account: "Account"
    card: "Card"
    content: str
    createdAt: datetime.datetime
    creator: "User"
    file: "File"
    title: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardDiffNotification(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class asOwner:
            """
            Type: bool
            """

            value = "asOwner"

        class card:
            """
            Type: Card
            """

            value = "card"

        class changers:
            """
            Type: list
            """

            value = "changers"

        class changes:
            """
            Type: str
            """

            value = "changes"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class lastUpdatedAt:
            """
            Type: datetime.datetime
            """

            value = "lastUpdatedAt"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    asOwner: bool
    card: "Card"
    changers: list
    changes: str
    createdAt: datetime.datetime
    lastUpdatedAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardHistory(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class card:
            """
            Type: Card
            """

            value = "card"

        class changer:
            """
            Type: User
            """

            value = "changer"

        class diff:
            """
            Type: str
            """

            value = "diff"

        class version:
            """
            Type: int
            """

            value = "version"

        class versionCreatedAt:
            """
            Type: datetime.datetime
            """

            value = "versionCreatedAt"

    account: "Account"
    card: "Card"
    changer: "User"
    diff: str
    version: int
    versionCreatedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardOrderInDeck(_BaseModel):
    class Fields(_PrintableEnum):
        class card:
            """
            Type: Card
            """

            value = "card"

        class changer:
            """
            Type: User
            """

            value = "changer"

        class deck:
            """
            Type: Deck
            """

            value = "deck"

        class sortIndex:
            """
            Type: str
            """

            value = "sortIndex"

    card: "Card"
    changer: "User"
    deck: "Deck"
    sortIndex: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardOrder(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class card:
            """
            Type: Card
            """

            value = "card"

        class label:
            """
            Type: str
            """

            value = "label"

        class sortValue:
            """
            Type: str
            """

            value = "sortValue"

    account: "Account"
    card: "Card"
    label: str
    sortValue: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardPreset(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class creator:
            """
            Type: User
            """

            value = "creator"

        class data:
            """
            Type: str
            """

            value = "data"

        class name:
            """
            Type: str
            """

            value = "name"

    account: "Account"
    createdAt: datetime.datetime
    creator: "User"
    data: str
    name: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardSubscription(_BaseModel):
    class Fields(_PrintableEnum):
        class card:
            """
            Type: Card
            """

            value = "card"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class user:
            """
            Type: User
            """

            value = "user"

    card: "Card"
    createdAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardUpvote(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class card:
            """
            Type: Card
            """

            value = "card"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class discordUserInfo:
            """
            Type: str
            """

            value = "discordUserInfo"

        class type:
            """
            Type: str
            """

            value = "type"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    card: "Card"
    createdAt: datetime.datetime
    discordUserInfo: str
    type: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Card(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class accountSeq:
            """
            Type: str
            """

            value = "accountSeq"

        class assignee:
            """
            Type: User
            """

            value = "assignee"

        class checkboxInfo:
            """
            Type: list
            """

            value = "checkboxInfo"

        class checkboxStats:
            """
            Type: str
            """

            value = "checkboxStats"

        class content:
            """
            Type: str
            """

            value = "content"

        class coverFile:
            """
            Type: File
            """

            value = "coverFile"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class creator:
            """
            Type: User
            """

            value = "creator"

        class deck:
            """
            Type: Deck
            """

            value = "deck"

        class discordGuild:
            """
            Type: DiscordGuild
            """

            value = "discordGuild"

        class dueDate:
            """
            Type: datetime.datetime
            """

            value = "dueDate"

        class effort:
            """
            Type: Any
            """

            value = "effort"

        class embeds:
            """
            Type: str
            """

            value = "embeds"

        class hasBlockingDeps:
            """
            Type: bool
            """

            value = "hasBlockingDeps"

        class isDoc:
            """
            Type: bool
            """

            value = "isDoc"

        class isPublic:
            """
            Type: bool
            """

            value = "isPublic"

        class lastUpdatedAt:
            """
            Type: datetime.datetime
            """

            value = "lastUpdatedAt"

        class legacyProject:
            """
            Type: Project
            """

            value = "legacyProject"

        class legacyProjectSeq:
            """
            Type: int
            """

            value = "legacyProjectSeq"

        class masterTags:
            """
            Type: list
            """

            value = "masterTags"

        class mentionedUsers:
            """
            Type: list
            """

            value = "mentionedUsers"

        class meta:
            """
            Type: str
            """

            value = "meta"

        class milestone:
            """
            Type: Milestone
            """

            value = "milestone"

        class parentCard:
            """
            Type: Card
            """

            value = "parentCard"

        class priority:
            """
            Type: str
            """

            value = "priority"

        class sourceWorkflowItemId:
            """
            Type: WorkflowItem
            """

            value = "sourceWorkflowItemId"

        class status:
            """
            Type: str
            """

            value = "status"

        class tags:
            """
            Type: list
            """

            value = "tags"

        class title:
            """
            Type: str
            """

            value = "title"

        class version:
            """
            Type: str
            """

            value = "version"

        class visibility:
            """
            Type: str
            """

            value = "visibility"

    class Relations(_PrintableEnum):
        class resolvables:
            """
            Type: Resolvable[]
            """

            value = "resolvables"

        class handCards:
            """
            Type: HandCard[]
            """

            value = "handCards"

        class timeTrackingSegments:
            """
            Type: TimeTrackingSegment[]
            """

            value = "timeTrackingSegments"

        class cardSubscriptions:
            """
            Type: CardSubscription[]
            """

            value = "cardSubscriptions"

        class resolvableEntries:
            """
            Type: ResolvableEntry[]
            """

            value = "resolvableEntries"

        class attachments:
            """
            Type: Attachment[]
            """

            value = "attachments"

        class diffs:
            """
            Type: CardHistory[]
            """

            value = "diffs"

        class totalTimeTrackingSums:
            """
            Type: TimeTrackingSum
            """

            value = "totalTimeTrackingSums"

        class userTimeTrackingSums:
            """
            Type: TimeTrackingSum[]
            """

            value = "userTimeTrackingSums"

        class childCards:
            """
            Type: Card[]
            """

            value = "childCards"

        class inDeps:
            """
            Type: Card[]
            """

            value = "inDeps"

        class outDeps:
            """
            Type: Card[]
            """

            value = "outDeps"

        class cardReferences:
            """
            Type: Card[]
            """

            value = "cardReferences"

        class upvotes:
            """
            Type: CardUpvote[]
            """

            value = "upvotes"

    account: "Account"
    accountSeq: str
    assignee: "User"
    checkboxInfo: list
    checkboxStats: str
    content: str
    coverFile: "File"
    createdAt: datetime.datetime
    creator: "User"
    deck: "Deck"
    discordGuild: "DiscordGuild"
    dueDate: datetime.datetime
    effort: Any
    embeds: str
    hasBlockingDeps: bool
    isDoc: bool
    isPublic: bool
    lastUpdatedAt: datetime.datetime
    legacyProject: "Project"
    legacyProjectSeq: int
    masterTags: list
    mentionedUsers: list
    meta: str
    milestone: "Milestone"
    parentCard: "Card"
    priority: str
    sourceWorkflowItemId: "WorkflowItem"
    status: str
    tags: list
    title: str
    version: str
    visibility: str
    resolvables: List["Resolvable"]
    handCards: List["HandCard"]
    timeTrackingSegments: List["TimeTrackingSegment"]
    cardSubscriptions: List["CardSubscription"]
    resolvableEntries: List["ResolvableEntry"]
    attachments: List["Attachment"]
    diffs: List["CardHistory"]
    totalTimeTrackingSums: "TimeTrackingSum"
    userTimeTrackingSums: List["TimeTrackingSum"]
    childCards: List["Card"]
    inDeps: List["Card"]
    outDeps: List["Card"]
    cardReferences: List["Card"]
    upvotes: List["CardUpvote"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardsEffortHistory(_BaseModel):
    class Fields(_PrintableEnum):
        class cardCount:
            """
            Type: int
            """

            value = "cardCount"

        class date:
            """
            Type: datetime.datetime
            """

            value = "date"

        class effortSum:
            """
            Type: int
            """

            value = "effortSum"

    cardCount: int
    date: datetime.datetime
    effortSum: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardsFinishedHistory(_BaseModel):
    class Fields(_PrintableEnum):
        class assignee:
            """
            Type: User
            """

            value = "assignee"

        class cardCount:
            """
            Type: int
            """

            value = "cardCount"

        class date:
            """
            Type: datetime.datetime
            """

            value = "date"

        class effortSum:
            """
            Type: int
            """

            value = "effortSum"

    assignee: "User"
    cardCount: int
    date: datetime.datetime
    effortSum: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardsStatusHistory(_BaseModel):
    class Fields(_PrintableEnum):
        class count:
            """
            Type: int
            """

            value = "count"

        class date:
            """
            Type: datetime.datetime
            """

            value = "date"

        class status:
            """
            Type: str
            """

            value = "status"

    count: int
    date: datetime.datetime
    status: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardsTimeToFinished(_BaseModel):
    class Fields(_PrintableEnum):
        class assignee:
            """
            Type: User
            """

            value = "assignee"

        class card:
            """
            Type: Card
            """

            value = "card"

        class doneAt:
            """
            Type: datetime.datetime
            """

            value = "doneAt"

        class effort:
            """
            Type: int
            """

            value = "effort"

        class startedAt:
            """
            Type: datetime.datetime
            """

            value = "startedAt"

    assignee: "User"
    card: "Card"
    doneAt: datetime.datetime
    effort: int
    startedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DailyDiscordGuildVoteMembership(_BaseModel):
    class Fields(_PrintableEnum):
        class discordGuild:
            """
            Type: DiscordGuild
            """

            value = "discordGuild"

        class membershipCount:
            """
            Type: int
            """

            value = "membershipCount"

        class t:
            """
            Type: datetime.datetime
            """

            value = "t"

    discordGuild: "DiscordGuild"
    membershipCount: int
    t: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DailyPublicProjectMembership(_BaseModel):
    class Fields(_PrintableEnum):
        class membershipCount:
            """
            Type: int
            """

            value = "membershipCount"

        class project:
            """
            Type: Project
            """

            value = "project"

        class t:
            """
            Type: datetime.datetime
            """

            value = "t"

    membershipCount: int
    project: "Project"
    t: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class PublicProjectVisit(_BaseModel):
    class Fields(_PrintableEnum):
        class project:
            """
            Type: Project
            """

            value = "project"

        class t:
            """
            Type: datetime.datetime
            """

            value = "t"

        class topReferrers:
            """
            Type: str
            """

            value = "topReferrers"

        class visitCounts:
            """
            Type: int
            """

            value = "visitCounts"

    project: "Project"
    t: datetime.datetime
    topReferrers: str
    visitCounts: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckAssignment(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class deck:
            """
            Type: Deck
            """

            value = "deck"

        class lastAssignedAt:
            """
            Type: datetime.datetime
            """

            value = "lastAssignedAt"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    deck: "Deck"
    lastAssignedAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckOrder(_BaseModel):
    class Fields(_PrintableEnum):
        class deck:
            """
            Type: Deck
            """

            value = "deck"

        class project:
            """
            Type: Project
            """

            value = "project"

        class sortIndex:
            """
            Type: str
            """

            value = "sortIndex"

        class user:
            """
            Type: User
            """

            value = "user"

    deck: "Deck"
    project: "Project"
    sortIndex: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckPublicOrder(_BaseModel):
    class Fields(_PrintableEnum):
        class deck:
            """
            Type: Deck
            """

            value = "deck"

        class project:
            """
            Type: Project
            """

            value = "project"

        class sortIndex:
            """
            Type: str
            """

            value = "sortIndex"

    deck: "Deck"
    project: "Project"
    sortIndex: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckSubscription(_BaseModel):
    class Fields(_PrintableEnum):
        class deck:
            """
            Type: Deck
            """

            value = "deck"

        class user:
            """
            Type: User
            """

            value = "user"

    deck: "Deck"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Deck(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class accountSeq:
            """
            Type: int
            """

            value = "accountSeq"

        class content:
            """
            Type: str
            """

            value = "content"

        class coverColor:
            """
            Type: str
            """

            value = "coverColor"

        class coverFile:
            """
            Type: File
            """

            value = "coverFile"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class creator:
            """
            Type: User
            """

            value = "creator"

        class defaultCard:
            """
            Type: str
            """

            value = "defaultCard"

        class defaultProjectTag:
            """
            Type: ProjectTag
            """

            value = "defaultProjectTag"

        class handSyncEnabled:
            """
            Type: bool
            """

            value = "handSyncEnabled"

        class isDeleted:
            """
            Type: bool
            """

            value = "isDeleted"

        class isOnboardingDeck:
            """
            Type: bool
            """

            value = "isOnboardingDeck"

        class manualOrderLabels:
            """
            Type: str
            """

            value = "manualOrderLabels"

        class milestone:
            """
            Type: Milestone
            """

            value = "milestone"

        class preferredOrder:
            """
            Type: Any
            """

            value = "preferredOrder"

        class project:
            """
            Type: Project
            """

            value = "project"

        class stats:
            """
            Type: str
            """

            value = "stats"

        class stickyDefaultProjectTag:
            """
            Type: bool
            """

            value = "stickyDefaultProjectTag"

        class title:
            """
            Type: str
            """

            value = "title"

    class Relations(_PrintableEnum):
        class cards:
            """
            Type: Card[]
            """

            value = "cards"

        class workflowItems:
            """
            Type: WorkflowItem[]
            """

            value = "workflowItems"

        class cardOrderInDecks:
            """
            Type: CardOrderInDeck[]
            """

            value = "cardOrderInDecks"

        class activities:
            """
            Type: Activity[]
            """

            value = "activities"

    account: "Account"
    accountSeq: int
    content: str
    coverColor: str
    coverFile: "File"
    createdAt: datetime.datetime
    creator: "User"
    defaultCard: str
    defaultProjectTag: "ProjectTag"
    handSyncEnabled: bool
    isDeleted: bool
    isOnboardingDeck: bool
    manualOrderLabels: str
    milestone: "Milestone"
    preferredOrder: Any
    project: "Project"
    stats: str
    stickyDefaultProjectTag: bool
    title: str
    cards: List["Card"]
    workflowItems: List["WorkflowItem"]
    cardOrderInDecks: List["CardOrderInDeck"]
    activities: List["Activity"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DiscordGuild(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class discordGuildId:
            """
            Type: str
            """

            value = "discordGuildId"

        class guildIconId:
            """
            Type: str
            """

            value = "guildIconId"

        class guildName:
            """
            Type: str
            """

            value = "guildName"

        class karmaRoleThresholds:
            """
            Type: str
            """

            value = "karmaRoleThresholds"

        class removeCommandEmoji:
            """
            Type: str
            """

            value = "removeCommandEmoji"

        class removeCommandEnabled:
            """
            Type: str
            """

            value = "removeCommandEnabled"

        class removeCommandRoleId:
            """
            Type: str
            """

            value = "removeCommandRoleId"

        class scope:
            """
            Type: str
            """

            value = "scope"

    class Relations(_PrintableEnum):
        class slashCommands:
            """
            Type: DiscordSlashCommand[]
            """

            value = "slashCommands"

        class projectNotifications:
            """
            Type: DiscordProjectNotification[]
            """

            value = "projectNotifications"

        class dailyDiscordGuildVoteMemberships:
            """
            Type: DailyDiscordGuildVoteMembership[]
            """

            value = "dailyDiscordGuildVoteMemberships"

        class members:
            """
            Type: DiscordMember[]
            """

            value = "members"

    account: "Account"
    createdAt: datetime.datetime
    discordGuildId: str
    guildIconId: str
    guildName: str
    karmaRoleThresholds: str
    removeCommandEmoji: str
    removeCommandEnabled: str
    removeCommandRoleId: str
    scope: str
    slashCommands: List["DiscordSlashCommand"]
    projectNotifications: List["DiscordProjectNotification"]
    dailyDiscordGuildVoteMemberships: List["DailyDiscordGuildVoteMembership"]
    members: List["DiscordMember"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DiscordMember(_BaseModel):
    class Fields(_PrintableEnum):
        class avatar:
            """
            Type: str
            """

            value = "avatar"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class deckyScore:
            """
            Type: int
            """

            value = "deckyScore"

        class discordGuild:
            """
            Type: DiscordGuild
            """

            value = "discordGuild"

        class discordUserId:
            """
            Type: str
            """

            value = "discordUserId"

        class discriminator:
            """
            Type: str
            """

            value = "discriminator"

        class name:
            """
            Type: str
            """

            value = "name"

        class nick:
            """
            Type: str
            """

            value = "nick"

    avatar: str
    createdAt: datetime.datetime
    deckyScore: int
    discordGuild: "DiscordGuild"
    discordUserId: str
    discriminator: str
    name: str
    nick: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DiscordProjectNotification(_BaseModel):
    class Fields(_PrintableEnum):
        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class disabledTypes:
            """
            Type: str
            """

            value = "disabledTypes"

        class discordChannelId:
            """
            Type: str
            """

            value = "discordChannelId"

        class discordGuild:
            """
            Type: DiscordGuild
            """

            value = "discordGuild"

        class project:
            """
            Type: Project
            """

            value = "project"

    createdAt: datetime.datetime
    disabledTypes: str
    discordChannelId: str
    discordGuild: "DiscordGuild"
    project: "Project"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DiscordSlashCommand(_BaseModel):
    class Fields(_PrintableEnum):
        class autoAddRoleToThread:
            """
            Type: str
            """

            value = "autoAddRoleToThread"

        class channelId:
            """
            Type: str
            """

            value = "channelId"

        class deck:
            """
            Type: Deck
            """

            value = "deck"

        class description:
            """
            Type: str
            """

            value = "description"

        class discordGuild:
            """
            Type: DiscordGuild
            """

            value = "discordGuild"

        class karmaForCompletion:
            """
            Type: int
            """

            value = "karmaForCompletion"

        class leaderboard:
            """
            Type: str
            """

            value = "leaderboard"

        class name:
            """
            Type: str
            """

            value = "name"

        class permissions:
            """
            Type: str
            """

            value = "permissions"

        class reaction:
            """
            Type: str
            """

            value = "reaction"

        class reactionThreshold:
            """
            Type: int
            """

            value = "reactionThreshold"

        class statusMessages:
            """
            Type: str
            """

            value = "statusMessages"

        class statusTargetChannelId:
            """
            Type: str
            """

            value = "statusTargetChannelId"

    autoAddRoleToThread: str
    channelId: str
    deck: "Deck"
    description: str
    discordGuild: "DiscordGuild"
    karmaForCompletion: int
    leaderboard: str
    name: str
    permissions: str
    reaction: str
    reactionThreshold: int
    statusMessages: str
    statusTargetChannelId: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DueCard(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class card:
            """
            Type: Card
            """

            value = "card"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    card: "Card"
    createdAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class File(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class deletedAt:
            """
            Type: datetime.datetime
            """

            value = "deletedAt"

        class deletedBy:
            """
            Type: User
            """

            value = "deletedBy"

        class isDeleted:
            """
            Type: bool
            """

            value = "isDeleted"

        class meta:
            """
            Type: str
            """

            value = "meta"

        class name:
            """
            Type: str
            """

            value = "name"

        class selfHosted:
            """
            Type: bool
            """

            value = "selfHosted"

        class size:
            """
            Type: str
            """

            value = "size"

        class uploader:
            """
            Type: User
            """

            value = "uploader"

        class url:
            """
            Type: str
            """

            value = "url"

    account: "Account"
    createdAt: datetime.datetime
    deletedAt: datetime.datetime
    deletedBy: "User"
    isDeleted: bool
    meta: str
    name: str
    selfHosted: bool
    size: str
    uploader: "User"
    url: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class HandCard(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class card:
            """
            Type: Card
            """

            value = "card"

        class sortIndex:
            """
            Type: int
            """

            value = "sortIndex"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    card: "Card"
    sortIndex: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Integration(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class creator:
            """
            Type: User
            """

            value = "creator"

        class disabled:
            """
            Type: str
            """

            value = "disabled"

        class type:
            """
            Type: str
            """

            value = "type"

        class user:
            """
            Type: User
            """

            value = "user"

        class userData:
            """
            Type: str
            """

            value = "userData"

        class version:
            """
            Type: int
            """

            value = "version"

    account: "Account"
    createdAt: datetime.datetime
    creator: "User"
    disabled: str
    type: str
    user: "User"
    userData: str
    version: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Invoice(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class chargeData:
            """
            Type: str
            """

            value = "chargeData"

        class charged:
            """
            Type: int
            """

            value = "charged"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class invoiceNumber:
            """
            Type: str
            """

            value = "invoiceNumber"

        class subtotal:
            """
            Type: int
            """

            value = "subtotal"

        class total:
            """
            Type: int
            """

            value = "total"

        class url:
            """
            Type: str
            """

            value = "url"

    account: "Account"
    chargeData: str
    charged: int
    createdAt: datetime.datetime
    invoiceNumber: str
    subtotal: int
    total: int
    url: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class LastSeenCardUpvote(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class lastSeenAt:
            """
            Type: datetime.datetime
            """

            value = "lastSeenAt"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    createdAt: datetime.datetime
    lastSeenAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class MilestoneProgress(_BaseModel):
    class Fields(_PrintableEnum):
        class milestone:
            """
            Type: Milestone
            """

            value = "milestone"

        class progress:
            """
            Type: str
            """

            value = "progress"

    milestone: "Milestone"
    progress: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class MilestoneProject(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class milestone:
            """
            Type: Milestone
            """

            value = "milestone"

        class project:
            """
            Type: Project
            """

            value = "project"

    account: "Account"
    milestone: "Milestone"
    project: "Project"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Milestone(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class accountSeq:
            """
            Type: int
            """

            value = "accountSeq"

        class color:
            """
            Type: str
            """

            value = "color"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class creator:
            """
            Type: User
            """

            value = "creator"

        class date:
            """
            Type: datetime.datetime
            """

            value = "date"

        class description:
            """
            Type: str
            """

            value = "description"

        class handSyncEnabled:
            """
            Type: bool
            """

            value = "handSyncEnabled"

        class isDeleted:
            """
            Type: str
            """

            value = "isDeleted"

        class isGlobal:
            """
            Type: bool
            """

            value = "isGlobal"

        class manualOrderLabels:
            """
            Type: str
            """

            value = "manualOrderLabels"

        class name:
            """
            Type: str
            """

            value = "name"

        class stats:
            """
            Type: str
            """

            value = "stats"

    class Relations(_PrintableEnum):
        class milestoneProjects:
            """
            Type: MilestoneProject[]
            """

            value = "milestoneProjects"

        class cards:
            """
            Type: Card[]
            """

            value = "cards"

        class activities:
            """
            Type: Activity[]
            """

            value = "activities"

        class progress:
            """
            Type: MilestoneProgress[]
            """

            value = "progress"

    account: "Account"
    accountSeq: int
    color: str
    createdAt: datetime.datetime
    creator: "User"
    date: datetime.datetime
    description: str
    handSyncEnabled: bool
    isDeleted: str
    isGlobal: bool
    manualOrderLabels: str
    name: str
    stats: str
    milestoneProjects: List["MilestoneProject"]
    cards: List["Card"]
    activities: List["Activity"]
    progress: List["MilestoneProgress"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectOrder(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class project:
            """
            Type: Project
            """

            value = "project"

        class sortIndex:
            """
            Type: str
            """

            value = "sortIndex"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    project: "Project"
    sortIndex: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectSelection(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class project:
            """
            Type: Project
            """

            value = "project"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    project: "Project"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectTag(_BaseModel):
    class Fields(_PrintableEnum):
        class color:
            """
            Type: str
            """

            value = "color"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class emoji:
            """
            Type: str
            """

            value = "emoji"

        class project:
            """
            Type: Project
            """

            value = "project"

        class tag:
            """
            Type: str
            """

            value = "tag"

    color: str
    createdAt: datetime.datetime
    emoji: str
    project: "Project"
    tag: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectUserSetting(_BaseModel):
    class Fields(_PrintableEnum):
        class project:
            """
            Type: Project
            """

            value = "project"

        class receivePublicProjectDigest:
            """
            Type: bool
            """

            value = "receivePublicProjectDigest"

        class user:
            """
            Type: User
            """

            value = "user"

    project: "Project"
    receivePublicProjectDigest: bool
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectUser(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class project:
            """
            Type: Project
            """

            value = "project"

        class projectRole:
            """
            Type: str
            """

            value = "projectRole"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    project: "Project"
    projectRole: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Project(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class accountSeq:
            """
            Type: int
            """

            value = "accountSeq"

        class allowUpvotes:
            """
            Type: bool
            """

            value = "allowUpvotes"

        class commentsArePublic:
            """
            Type: bool
            """

            value = "commentsArePublic"

        class coverFile:
            """
            Type: File
            """

            value = "coverFile"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class defaultUserAccess:
            """
            Type: str
            """

            value = "defaultUserAccess"

        class id:
            """
            Type: str
            """

            value = "id"

        class isPublic:
            """
            Type: bool
            """

            value = "isPublic"

        class markerColor:
            """
            Type: Any
            """

            value = "markerColor"

        class name:
            """
            Type: str
            """

            value = "name"

        class publicBackgroundColor:
            """
            Type: str
            """

            value = "publicBackgroundColor"

        class publicBackgroundImage:
            """
            Type: File
            """

            value = "publicBackgroundImage"

        class publicBannerFile:
            """
            Type: File
            """

            value = "publicBannerFile"

        class publicHeading:
            """
            Type: str
            """

            value = "publicHeading"

        class publicIsExplicit:
            """
            Type: bool
            """

            value = "publicIsExplicit"

        class publicLayoutVersion:
            """
            Type: int
            """

            value = "publicLayoutVersion"

        class publicMessage:
            """
            Type: str
            """

            value = "publicMessage"

        class publicPath:
            """
            Type: str
            """

            value = "publicPath"

        class publicRegistryAgreement:
            """
            Type: bool
            """

            value = "publicRegistryAgreement"

        class publicTileFile:
            """
            Type: File
            """

            value = "publicTileFile"

        class visibility:
            """
            Type: str
            """

            value = "visibility"

    class Relations(_PrintableEnum):
        class decks:
            """
            Type: Deck[]
            """

            value = "decks"

        class deckPublicOrders:
            """
            Type: DeckPublicOrder[]
            """

            value = "deckPublicOrders"

        class milestoneProjects:
            """
            Type: MilestoneProject[]
            """

            value = "milestoneProjects"

        class publicProjectVisits:
            """
            Type: PublicProjectVisit[]
            """

            value = "publicProjectVisits"

        class dailyPublicProjectMembership:
            """
            Type: DailyPublicProjectMembership[]
            """

            value = "dailyPublicProjectMembership"

        class publicProjectMemberships:
            """
            Type: PublicProjectMembership[]
            """

            value = "publicProjectMemberships"

        class cardUpvotes:
            """
            Type: CardUpvote[]
            """

            value = "cardUpvotes"

        class cards:
            """
            Type: Card[]
            """

            value = "cards"

        class tags:
            """
            Type: ProjectTag[]
            """

            value = "tags"

        class activities:
            """
            Type: Activity[]
            """

            value = "activities"

        class explicitProjectUsers:
            """
            Type: ProjectUser[]
            """

            value = "explicitProjectUsers"

        class access:
            """
            Type: UserProjectAccess[]
            """

            value = "access"

        class publicProjectInfo:
            """
            Type: PublicProjectInfo
            """

            value = "publicProjectInfo"

    account: "Account"
    accountSeq: int
    allowUpvotes: bool
    commentsArePublic: bool
    coverFile: "File"
    createdAt: datetime.datetime
    defaultUserAccess: str
    id: str
    isPublic: bool
    markerColor: Any
    name: str
    publicBackgroundColor: str
    publicBackgroundImage: "File"
    publicBannerFile: "File"
    publicHeading: str
    publicIsExplicit: bool
    publicLayoutVersion: int
    publicMessage: str
    publicPath: str
    publicRegistryAgreement: bool
    publicTileFile: "File"
    visibility: str
    decks: List["Deck"]
    deckPublicOrders: List["DeckPublicOrder"]
    milestoneProjects: List["MilestoneProject"]
    publicProjectVisits: List["PublicProjectVisit"]
    dailyPublicProjectMembership: List["DailyPublicProjectMembership"]
    publicProjectMemberships: List["PublicProjectMembership"]
    cardUpvotes: List["CardUpvote"]
    cards: List["Card"]
    tags: List["ProjectTag"]
    activities: List["Activity"]
    explicitProjectUsers: List["ProjectUser"]
    access: List["UserProjectAccess"]
    publicProjectInfo: "PublicProjectInfo"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class PublicProjectInfo(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class activities7d:
            """
            Type: str
            """

            value = "activities7d"

        class cardCount:
            """
            Type: str
            """

            value = "cardCount"

        class cardDoneStreak:
            """
            Type: str
            """

            value = "cardDoneStreak"

        class lastActivityAt:
            """
            Type: str
            """

            value = "lastActivityAt"

        class project:
            """
            Type: Project
            """

            value = "project"

        class visits7d:
            """
            Type: str
            """

            value = "visits7d"

    account: "Account"
    activities7d: str
    cardCount: str
    cardDoneStreak: str
    lastActivityAt: str
    project: "Project"
    visits7d: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class PublicProjectMembership(_BaseModel):
    class Fields(_PrintableEnum):
        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class digestFrequencyInDays:
            """
            Type: int
            """

            value = "digestFrequencyInDays"

        class project:
            """
            Type: Project
            """

            value = "project"

        class user:
            """
            Type: User
            """

            value = "user"

    createdAt: datetime.datetime
    digestFrequencyInDays: int
    project: "Project"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class QueueEntry(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class card:
            """
            Type: Card
            """

            value = "card"

        class cardDoneAt:
            """
            Type: datetime.datetime
            """

            value = "cardDoneAt"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class isCleared:
            """
            Type: bool
            """

            value = "isCleared"

        class sortIndex:
            """
            Type: int
            """

            value = "sortIndex"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    card: "Card"
    cardDoneAt: datetime.datetime
    createdAt: datetime.datetime
    isCleared: bool
    sortIndex: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class QueueSelection(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class queueUser:
            """
            Type: User
            """

            value = "queueUser"

        class sortIndex:
            """
            Type: int
            """

            value = "sortIndex"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    queueUser: "User"
    sortIndex: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Release(_BaseModel):
    class Fields(_PrintableEnum):
        class content:
            """
            Type: str
            """

            value = "content"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class isLive:
            """
            Type: str
            """

            value = "isLive"

        class title:
            """
            Type: str
            """

            value = "title"

        class version:
            """
            Type: str
            """

            value = "version"

    content: str
    createdAt: datetime.datetime
    isLive: str
    title: str
    version: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableEntryHistory(_BaseModel):
    class Fields(_PrintableEnum):
        class author:
            """
            Type: User
            """

            value = "author"

        class content:
            """
            Type: str
            """

            value = "content"

        class lastChangedAt:
            """
            Type: datetime.datetime
            """

            value = "lastChangedAt"

        class resolvable:
            """
            Type: Resolvable
            """

            value = "resolvable"

        class version:
            """
            Type: int
            """

            value = "version"

    author: "User"
    content: str
    lastChangedAt: datetime.datetime
    resolvable: "Resolvable"
    version: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableEntry(_BaseModel):
    class Fields(_PrintableEnum):
        class author:
            """
            Type: User
            """

            value = "author"

        class content:
            """
            Type: str
            """

            value = "content"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class lastChangedAt:
            """
            Type: datetime.datetime
            """

            value = "lastChangedAt"

        class meta:
            """
            Type: str
            """

            value = "meta"

        class resolvable:
            """
            Type: Resolvable
            """

            value = "resolvable"

        class version:
            """
            Type: str
            """

            value = "version"

    class Relations(_PrintableEnum):
        class histories:
            """
            Type: ResolvableEntryHistory[]
            """

            value = "histories"

    author: "User"
    content: str
    createdAt: datetime.datetime
    lastChangedAt: datetime.datetime
    meta: str
    resolvable: "Resolvable"
    version: str
    histories: List["ResolvableEntryHistory"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableNotification(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class isLastParticipant:
            """
            Type: bool
            """

            value = "isLastParticipant"

        class isParticipating:
            """
            Type: bool
            """

            value = "isParticipating"

        class isSnoozing:
            """
            Type: bool
            """

            value = "isSnoozing"

        class lastUpdatedAt:
            """
            Type: datetime.datetime
            """

            value = "lastUpdatedAt"

        class latestEntry:
            """
            Type: ResolvableEntry
            """

            value = "latestEntry"

        class latestSeenEntry:
            """
            Type: ResolvableEntry
            """

            value = "latestSeenEntry"

        class resolvable:
            """
            Type: Resolvable
            """

            value = "resolvable"

        class snoozeUntil:
            """
            Type: datetime.datetime
            """

            value = "snoozeUntil"

        class unseenAuthors:
            """
            Type: list
            """

            value = "unseenAuthors"

        class unseenEntryCount:
            """
            Type: int
            """

            value = "unseenEntryCount"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    createdAt: datetime.datetime
    isLastParticipant: bool
    isParticipating: bool
    isSnoozing: bool
    lastUpdatedAt: datetime.datetime
    latestEntry: "ResolvableEntry"
    latestSeenEntry: "ResolvableEntry"
    resolvable: "Resolvable"
    snoozeUntil: datetime.datetime
    unseenAuthors: list
    unseenEntryCount: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableParticipantHistory(_BaseModel):
    class Fields(_PrintableEnum):
        class addedBy:
            """
            Type: User
            """

            value = "addedBy"

        class done:
            """
            Type: bool
            """

            value = "done"

        class firstJoinedAt:
            """
            Type: str
            """

            value = "firstJoinedAt"

        class lastChangedAt:
            """
            Type: datetime.datetime
            """

            value = "lastChangedAt"

        class resolvable:
            """
            Type: Resolvable
            """

            value = "resolvable"

        class user:
            """
            Type: User
            """

            value = "user"

        class version:
            """
            Type: int
            """

            value = "version"

    addedBy: "User"
    done: bool
    firstJoinedAt: str
    lastChangedAt: datetime.datetime
    resolvable: "Resolvable"
    user: "User"
    version: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableParticipant(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class addedBy:
            """
            Type: User
            """

            value = "addedBy"

        class discordUserId:
            """
            Type: str
            """

            value = "discordUserId"

        class done:
            """
            Type: bool
            """

            value = "done"

        class firstJoinedAt:
            """
            Type: str
            """

            value = "firstJoinedAt"

        class lastChangedAt:
            """
            Type: str
            """

            value = "lastChangedAt"

        class resolvable:
            """
            Type: Resolvable
            """

            value = "resolvable"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    addedBy: "User"
    discordUserId: str
    done: bool
    firstJoinedAt: str
    lastChangedAt: str
    resolvable: "Resolvable"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Resolvable(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class card:
            """
            Type: Card
            """

            value = "card"

        class closedAt:
            """
            Type: datetime.datetime
            """

            value = "closedAt"

        class closedBy:
            """
            Type: User
            """

            value = "closedBy"

        class context:
            """
            Type: str
            """

            value = "context"

        class contextAsPrio:
            """
            Type: str
            """

            value = "contextAsPrio"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class creator:
            """
            Type: User
            """

            value = "creator"

        class isClosed:
            """
            Type: str
            """

            value = "isClosed"

        class isPublic:
            """
            Type: bool
            """

            value = "isPublic"

    class Relations(_PrintableEnum):
        class participants:
            """
            Type: ResolvableParticipant[]
            """

            value = "participants"

        class participantHistories:
            """
            Type: ResolvableParticipantHistory[]
            """

            value = "participantHistories"

        class entries:
            """
            Type: ResolvableEntry[]
            """

            value = "entries"

    account: "Account"
    card: "Card"
    closedAt: datetime.datetime
    closedBy: "User"
    context: str
    contextAsPrio: str
    createdAt: datetime.datetime
    creator: "User"
    isClosed: str
    isPublic: bool
    participants: List["ResolvableParticipant"]
    participantHistories: List["ResolvableParticipantHistory"]
    entries: List["ResolvableEntry"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class SavedSearch(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class forceOr:
            """
            Type: bool
            """

            value = "forceOr"

        class owner:
            """
            Type: User
            """

            value = "owner"

        class tokens:
            """
            Type: list
            """

            value = "tokens"

    account: "Account"
    forceOr: bool
    owner: "User"
    tokens: list

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class StripeAccountSync(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class billingCycleEnd:
            """
            Type: datetime.datetime
            """

            value = "billingCycleEnd"

        class billingCycleStart:
            """
            Type: datetime.datetime
            """

            value = "billingCycleStart"

        class centsPerSeat:
            """
            Type: int
            """

            value = "centsPerSeat"

        class euVatIdData:
            """
            Type: str
            """

            value = "euVatIdData"

        class grossActualBalance:
            """
            Type: int
            """

            value = "grossActualBalance"

        class grossBonusBalance:
            """
            Type: int
            """

            value = "grossBonusBalance"

        class hasBeenCancelledAt:
            """
            Type: datetime.datetime
            """

            value = "hasBeenCancelledAt"

        class netGiftBalance:
            """
            Type: int
            """

            value = "netGiftBalance"

        class paymentMethod:
            """
            Type: str
            """

            value = "paymentMethod"

        class pendingPlanType:
            """
            Type: str
            """

            value = "pendingPlanType"

        class planName:
            """
            Type: str
            """

            value = "planName"

        class planType:
            """
            Type: str
            """

            value = "planType"

        class repeatingCoupon:
            """
            Type: str
            """

            value = "repeatingCoupon"

        class status:
            """
            Type: str
            """

            value = "status"

        class vatCountryCode:
            """
            Type: str
            """

            value = "vatCountryCode"

        class vatTaxPercentage:
            """
            Type: int
            """

            value = "vatTaxPercentage"

    account: "Account"
    billingCycleEnd: datetime.datetime
    billingCycleStart: datetime.datetime
    centsPerSeat: int
    euVatIdData: str
    grossActualBalance: int
    grossBonusBalance: int
    hasBeenCancelledAt: datetime.datetime
    netGiftBalance: int
    paymentMethod: str
    pendingPlanType: str
    planName: str
    planType: str
    repeatingCoupon: str
    status: str
    vatCountryCode: str
    vatTaxPercentage: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class TimeTrackingSegment(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class addedManually:
            """
            Type: bool
            """

            value = "addedManually"

        class card:
            """
            Type: Card
            """

            value = "card"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class finishedAt:
            """
            Type: datetime.datetime
            """

            value = "finishedAt"

        class modifyDurationMsBy:
            """
            Type: int
            """

            value = "modifyDurationMsBy"

        class startedAt:
            """
            Type: datetime.datetime
            """

            value = "startedAt"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    addedManually: bool
    card: "Card"
    createdAt: datetime.datetime
    finishedAt: datetime.datetime
    modifyDurationMsBy: int
    startedAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class TimeTrackingSum(_BaseModel):
    class Fields(_PrintableEnum):
        class card:
            """
            Type: Card
            """

            value = "card"

        class runningModifyDurationMsBy:
            """
            Type: int
            """

            value = "runningModifyDurationMsBy"

        class runningStartedAt:
            """
            Type: datetime.datetime
            """

            value = "runningStartedAt"

        class sumMs:
            """
            Type: int
            """

            value = "sumMs"

        class user:
            """
            Type: User
            """

            value = "user"

    card: "Card"
    runningModifyDurationMsBy: int
    runningStartedAt: datetime.datetime
    sumMs: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserDismissedHint(_BaseModel):
    class Fields(_PrintableEnum):
        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class hintKey:
            """
            Type: str
            """

            value = "hintKey"

        class returnAt:
            """
            Type: datetime.datetime
            """

            value = "returnAt"

        class user:
            """
            Type: User
            """

            value = "user"

    createdAt: datetime.datetime
    hintKey: str
    returnAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserEmail(_BaseModel):
    class Fields(_PrintableEnum):
        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class email:
            """
            Type: str
            """

            value = "email"

        class isPrimary:
            """
            Type: str
            """

            value = "isPrimary"

        class isVerified:
            """
            Type: str
            """

            value = "isVerified"

        class user:
            """
            Type: User
            """

            value = "user"

    createdAt: datetime.datetime
    email: str
    isPrimary: str
    isVerified: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserInvitation(_BaseModel):
    class Fields(_PrintableEnum):
        class accessToProjectIds:
            """
            Type: list
            """

            value = "accessToProjectIds"

        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class email:
            """
            Type: str
            """

            value = "email"

        class inviter:
            """
            Type: User
            """

            value = "inviter"

        class role:
            """
            Type: str
            """

            value = "role"

    accessToProjectIds: list
    account: "Account"
    createdAt: datetime.datetime
    email: str
    inviter: "User"
    role: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserInviteCode(_BaseModel):
    class Fields(_PrintableEnum):
        class accessToProjectIds:
            """
            Type: list
            """

            value = "accessToProjectIds"

        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class creator:
            """
            Type: User
            """

            value = "creator"

        class isActive:
            """
            Type: bool
            """

            value = "isActive"

        class role:
            """
            Type: str
            """

            value = "role"

        class token:
            """
            Type: str
            """

            value = "token"

        class useCount:
            """
            Type: int
            """

            value = "useCount"

        class validUntil:
            """
            Type: datetime.datetime
            """

            value = "validUntil"

    accessToProjectIds: list
    account: "Account"
    createdAt: datetime.datetime
    creator: "User"
    isActive: bool
    role: str
    token: str
    useCount: int
    validUntil: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserOnboarding(_BaseModel):
    class Fields(_PrintableEnum):
        class steps:
            """
            Type: str
            """

            value = "steps"

        class user:
            """
            Type: User
            """

            value = "user"

    steps: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserProjectAccess(_BaseModel):
    class Fields(_PrintableEnum):
        class project:
            """
            Type: Project
            """

            value = "project"

        class projectRole:
            """
            Type: str
            """

            value = "projectRole"

        class role:
            """
            Type: str
            """

            value = "role"

        class user:
            """
            Type: User
            """

            value = "user"

    project: "Project"
    projectRole: str
    role: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserTag(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class tag:
            """
            Type: str
            """

            value = "tag"

        class user:
            """
            Type: User
            """

            value = "user"

    account: "Account"
    createdAt: datetime.datetime
    tag: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class User(_BaseModel):
    class Fields(_PrintableEnum):
        class autoMeFilterCardLimit:
            """
            Type: int
            """

            value = "autoMeFilterCardLimit"

        class cdxRole:
            """
            Type: str
            """

            value = "cdxRole"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class disableAnimations:
            """
            Type: bool
            """

            value = "disableAnimations"

        class disableMovingImages:
            """
            Type: bool
            """

            value = "disableMovingImages"

        class disableSpellcheck:
            """
            Type: bool
            """

            value = "disableSpellcheck"

        class fullName:
            """
            Type: str
            """

            value = "fullName"

        class hasPassword:
            """
            Type: str
            """

            value = "hasPassword"

        class isIntegration:
            """
            Type: bool
            """

            value = "isIntegration"

        class lastSeenRelease:
            """
            Type: Release
            """

            value = "lastSeenRelease"

        class name:
            """
            Type: str
            """

            value = "name"

        class profileImage:
            """
            Type: File
            """

            value = "profileImage"

        class showCardIdInTimer:
            """
            Type: bool
            """

            value = "showCardIdInTimer"

        class statusColorPalette:
            """
            Type: str
            """

            value = "statusColorPalette"

        class timezone:
            """
            Type: str
            """

            value = "timezone"

        class wantsConvoDigestMail:
            """
            Type: bool
            """

            value = "wantsConvoDigestMail"

        class wantsDailyDigestMail:
            """
            Type: bool
            """

            value = "wantsDailyDigestMail"

        class wantsNewsletter:
            """
            Type: bool
            """

            value = "wantsNewsletter"

    class Relations(_PrintableEnum):
        class deckOrders:
            """
            Type: DeckOrder[]
            """

            value = "deckOrders"

        class projectOrders:
            """
            Type: ProjectOrder[]
            """

            value = "projectOrders"

        class projectSelections:
            """
            Type: ProjectSelection[]
            """

            value = "projectSelections"

        class queueSelections:
            """
            Type: QueueSelection[]
            """

            value = "queueSelections"

        class accountRoles:
            """
            Type: AccountRole[]
            """

            value = "accountRoles"

        class cardDiffNotifications:
            """
            Type: CardDiffNotification[]
            """

            value = "cardDiffNotifications"

        class resolvableNotifications:
            """
            Type: ResolvableNotification[]
            """

            value = "resolvableNotifications"

        class publicProjectMembership:
            """
            Type: PublicProjectMembership[]
            """

            value = "publicProjectMembership"

        class lastSeenCardUpvotes:
            """
            Type: LastSeenCardUpvote[]
            """

            value = "lastSeenCardUpvotes"

        class dueCards:
            """
            Type: DueCard[]
            """

            value = "dueCards"

        class savedSearches:
            """
            Type: SavedSearch[]
            """

            value = "savedSearches"

        class activities:
            """
            Type: Activity[]
            """

            value = "activities"

        class emails:
            """
            Type: UserEmail[]
            """

            value = "emails"

        class tags:
            """
            Type: UserTag[]
            """

            value = "tags"

        class unverifiedEmails:
            """
            Type: UserEmail[]
            """

            value = "unverifiedEmails"

        class primaryEmail:
            """
            Type: UserEmail
            """

            value = "primaryEmail"

        class pinnedMilestone:
            """
            Type: Milestone
            """

            value = "pinnedMilestone"

        class explicitProjectAccess:
            """
            Type: ProjectUser[]
            """

            value = "explicitProjectAccess"

        class withProjectAccess:
            """
            Type: UserProjectAccess[]
            """

            value = "withProjectAccess"

        class projectSettings:
            """
            Type: ProjectUserSetting[]
            """

            value = "projectSettings"

        class accountSettings:
            """
            Type: AccountUserSetting[]
            """

            value = "accountSettings"

        class dismissedHints:
            """
            Type: UserDismissedHint[]
            """

            value = "dismissedHints"

        class slackIntegrations:
            """
            Type: Integration[]
            """

            value = "slackIntegrations"

        class activeTimeTracker:
            """
            Type: ActiveTimeTracker
            """

            value = "activeTimeTracker"

        class participations:
            """
            Type: ResolvableParticipant[]
            """

            value = "participations"

        class upvotes:
            """
            Type: CardUpvote[]
            """

            value = "upvotes"

        class userOnboarding:
            """
            Type: UserOnboarding
            """

            value = "userOnboarding"

    autoMeFilterCardLimit: int
    cdxRole: str
    createdAt: datetime.datetime
    disableAnimations: bool
    disableMovingImages: bool
    disableSpellcheck: bool
    fullName: str
    hasPassword: str
    isIntegration: bool
    lastSeenRelease: "Release"
    name: str
    profileImage: "File"
    showCardIdInTimer: bool
    statusColorPalette: str
    timezone: str
    wantsConvoDigestMail: bool
    wantsDailyDigestMail: bool
    wantsNewsletter: bool
    deckOrders: List["DeckOrder"]
    projectOrders: List["ProjectOrder"]
    projectSelections: List["ProjectSelection"]
    queueSelections: List["QueueSelection"]
    accountRoles: List["AccountRole"]
    cardDiffNotifications: List["CardDiffNotification"]
    resolvableNotifications: List["ResolvableNotification"]
    publicProjectMembership: List["PublicProjectMembership"]
    lastSeenCardUpvotes: List["LastSeenCardUpvote"]
    dueCards: List["DueCard"]
    savedSearches: List["SavedSearch"]
    activities: List["Activity"]
    emails: List["UserEmail"]
    tags: List["UserTag"]
    unverifiedEmails: List["UserEmail"]
    primaryEmail: "UserEmail"
    pinnedMilestone: "Milestone"
    explicitProjectAccess: List["ProjectUser"]
    withProjectAccess: List["UserProjectAccess"]
    projectSettings: List["ProjectUserSetting"]
    accountSettings: List["AccountUserSetting"]
    dismissedHints: List["UserDismissedHint"]
    slackIntegrations: List["Integration"]
    activeTimeTracker: "ActiveTimeTracker"
    participations: List["ResolvableParticipant"]
    upvotes: List["CardUpvote"]
    userOnboarding: "UserOnboarding"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserReportEmail(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class email:
            """
            Type: str
            """

            value = "email"

        class enabled:
            """
            Type: str
            """

            value = "enabled"

        class userReportSetting:
            """
            Type: UserReportSetting
            """

            value = "userReportSetting"

    account: "Account"
    createdAt: datetime.datetime
    email: str
    enabled: str
    userReportSetting: "UserReportSetting"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserReportSetting(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class deckMapping:
            """
            Type: str
            """

            value = "deckMapping"

        class fileSizeBytesLimit:
            """
            Type: int
            """

            value = "fileSizeBytesLimit"

        class id:
            """
            Type: str
            """

            value = "id"

        class name:
            """
            Type: str
            """

            value = "name"

        class prioMapping:
            """
            Type: str
            """

            value = "prioMapping"

    class Relations(_PrintableEnum):
        class reportTokens:
            """
            Type: UserReportToken[]
            """

            value = "reportTokens"

    account: "Account"
    createdAt: datetime.datetime
    deckMapping: str
    fileSizeBytesLimit: int
    id: str
    name: str
    prioMapping: str
    reportTokens: List["UserReportToken"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserReportToken(_BaseModel):
    class Fields(_PrintableEnum):
        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class enabled:
            """
            Type: str
            """

            value = "enabled"

        class label:
            """
            Type: str
            """

            value = "label"

        class reportCount:
            """
            Type: int
            """

            value = "reportCount"

        class userReportSetting:
            """
            Type: UserReportSetting
            """

            value = "userReportSetting"

    createdAt: datetime.datetime
    enabled: str
    label: str
    reportCount: int
    userReportSetting: "UserReportSetting"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Wizard(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class currentStep:
            """
            Type: str
            """

            value = "currentStep"

        class data:
            """
            Type: str
            """

            value = "data"

        class finishedAt:
            """
            Type: datetime.datetime
            """

            value = "finishedAt"

        class name:
            """
            Type: str
            """

            value = "name"

    account: "Account"
    createdAt: datetime.datetime
    currentStep: str
    data: str
    finishedAt: datetime.datetime
    name: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class WorkflowItemHistory(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class changer:
            """
            Type: User
            """

            value = "changer"

        class diff:
            """
            Type: str
            """

            value = "diff"

        class version:
            """
            Type: int
            """

            value = "version"

        class versionCreatedAt:
            """
            Type: datetime.datetime
            """

            value = "versionCreatedAt"

    account: "Account"
    changer: "User"
    diff: str
    version: int
    versionCreatedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class WorkflowItem(_BaseModel):
    class Fields(_PrintableEnum):
        class account:
            """
            Type: Account
            """

            value = "account"

        class accountSeq:
            """
            Type: str
            """

            value = "accountSeq"

        class assignee:
            """
            Type: User
            """

            value = "assignee"

        class checkboxInfo:
            """
            Type: list
            """

            value = "checkboxInfo"

        class checkboxStats:
            """
            Type: str
            """

            value = "checkboxStats"

        class content:
            """
            Type: str
            """

            value = "content"

        class createdAt:
            """
            Type: datetime.datetime
            """

            value = "createdAt"

        class creator:
            """
            Type: User
            """

            value = "creator"

        class deck:
            """
            Type: Deck
            """

            value = "deck"

        class effort:
            """
            Type: Any
            """

            value = "effort"

        class lastUpdatedAt:
            """
            Type: datetime.datetime
            """

            value = "lastUpdatedAt"

        class masterTags:
            """
            Type: list
            """

            value = "masterTags"

        class mentionedUsers:
            """
            Type: list
            """

            value = "mentionedUsers"

        class priority:
            """
            Type: str
            """

            value = "priority"

        class sortOrder:
            """
            Type: str
            """

            value = "sortOrder"

        class tags:
            """
            Type: list
            """

            value = "tags"

        class targetDeck:
            """
            Type: Deck
            """

            value = "targetDeck"

        class title:
            """
            Type: str
            """

            value = "title"

        class version:
            """
            Type: str
            """

            value = "version"

        class visibility:
            """
            Type: str
            """

            value = "visibility"

    class Relations(_PrintableEnum):
        class diffs:
            """
            Type: WorkflowItemHistory[]
            """

            value = "diffs"

        class inDeps:
            """
            Type: WorkflowItem[]
            """

            value = "inDeps"

        class outDeps:
            """
            Type: WorkflowItem[]
            """

            value = "outDeps"

    account: "Account"
    accountSeq: str
    assignee: "User"
    checkboxInfo: list
    checkboxStats: str
    content: str
    createdAt: datetime.datetime
    creator: "User"
    deck: "Deck"
    effort: Any
    lastUpdatedAt: datetime.datetime
    masterTags: list
    mentionedUsers: list
    priority: str
    sortOrder: str
    tags: list
    targetDeck: "Deck"
    title: str
    version: str
    visibility: str
    diffs: List["WorkflowItemHistory"]
    inDeps: List["WorkflowItem"]
    outDeps: List["WorkflowItem"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)
