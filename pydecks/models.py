import datetime
from typing import Any, List
import sys
import inspect

from .utils import is_valid_uuid, pascalize

from weakref import WeakValueDictionary


class _ModelCache:
    _instance = None
    __model_cache = WeakValueDictionary()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(_ModelCache, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def get(cls, model_name, id, data=None):
        if id in cls.__model_cache:
            if data:
                cls.__model_cache[id].update(data)
            return cls.__model_cache[id]
        else:
            model_name = pascalize(model_name)
            model_class = model_classes.get(model_name)
            if not model_class:
                raise ValueError(f"No model found for {model_name}")
            model = model_class(id, data)
            cls.__model_cache[id] = model
            return model

    @classmethod
    def exists(cls, id):
        return id in cls.__model_cache

    @classmethod
    def get_id(cls, id, default=None):
        return cls.__model_cache.get(id, default)

    def __len__(self):
        return len(self.__model_cache)

    def __iter__(self):
        return iter(self.__model_cache.values())

    def __str__(self):
        return f"<ModelCache: {len(self.__model_cache)} items>"

    def __repr__(self):
        return str(self)

    def __contains__(self, item):
        return item in self.__model_cache


class _BaseModel:
    def __init__(self, id, data=None):
        self.id = id
        if data:
            self.update(data)

    def update(self, data):
        for key, value in data.items():
            if key == "id":
                setattr(self, key, value)
            elif is_valid_uuid(value):
                setattr(self, key, model_cache.get(value))
            elif isinstance(value, list):
                for item in value:
                    if is_valid_uuid(item):
                        setattr(self, key, model_cache.get(item))
                    else:
                        setattr(self, key, value)

    def properties(self):
        return [
            prop
            for prop in dir(self)
            if not prop.startswith("__") and not callable(getattr(self, prop))
        ]

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.id}>"

    def __repr__(self):
        return f"""{self.__class__.__name__}: {self.id} {{
    {''',
'''.join([f"    {prop}: {getattr(self, prop)}" for prop in self.properties()])}
}}"""


class _root(_BaseModel):
    def __init__(self, **kwargs):
        self.releases: List[Release]
        self.accountOnboardingSteps: List[AccountOnboardingStep]
        self.account: Account
        self.loggedInUser: User
        self.cardsStatusHistory: List[CardsStatusHistory]
        self.cardsEffortHistory: List[CardsEffortHistory]
        self.cardsFinishedHistory: List[CardsFinishedHistory]
        self.cardsTimeToFinished: List[CardsTimeToFinished]


class AccountOnboardingStep(_BaseModel):
    def __init__(self, **kwargs):
        self.chapter: str
        self.description: str
        self.milestone: str
        self.sortValue: str
        self.title: str
        self.variants: list
        self.xp: int


class AccountOnboarding(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.steps: str
        self.variants: list


class AccountRole(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.createdAt: datetime.datetime
        self.isBillingContact: str
        self.lastChangedAt: datetime.datetime
        self.role: str
        self.user: User


class AccountSetting(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.key: str
        self.usesDefault: str
        self.value: str


class AccountUserAchievement(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.context: str
        self.user: User
        self.value: str


class AccountUserSetting(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.inboxDeck: Deck
        self.user: User


class Account(_BaseModel):
    def __init__(self, **kwargs):
        self.activeFeatureFlags: str
        self.activeProjectCount: int
        self.allowInheritHeroCover: bool
        self.attachmentCoverMode: str
        self.billingCity: str
        self.billingCountryCode: str
        self.billingLine1: str
        self.billingLine2: str
        self.billingName: str
        self.billingType: str
        self.billingZip: str
        self.coupon: str
        self.createdAt: datetime.datetime
        self.dependenciesEnabled: bool
        self.disabledAt: datetime.datetime
        self.disabledBy: User
        self.effortScale: str
        self.hideCompletedCardCountForDecks: bool
        self.id: str
        self.isDisabled: bool
        self.isLearning: bool
        self.isNonProfit: bool
        self.maxHandSlotCount: int
        self.maxTimeTrackingSegmentMsDuration: int
        self.milestonesEnabled: bool
        self.name: str
        self.netGiftAmount: str
        self.offeringTrial: bool
        self.persona: str
        self.priorityLabels: str
        self.seats: int
        self.staffPermission: str
        self.statusChangeDurations: str
        self.subdomain: str
        self.timeTrackingMode: str
        self.timeTrackingSwimLaneInfo: bool
        self.totalMediaByteUsage: int
        self.workdays: str
        self.workflowMode: str
        self.cards: List[Card]
        self.invoices: List[Invoice]
        self.cardPresets: List[CardPreset]
        self.attachments: List[Attachment]
        self.discordGuilds: List[DiscordGuild]
        self.timeTrackingSegments: List[TimeTrackingSegment]
        self.workflowItems: List[WorkflowItem]
        self.deckAssignments: List[DeckAssignment]
        self.assigneeAssignments: List[AssigneeAssignment]
        self.assigneeDeckAssignments: List[AssigneeDeckAssignment]
        self.wizards: List[Wizard]
        self.milestones: List[Milestone]
        self.handCards: List[HandCard]
        self.resolvables: List[Resolvable]
        self.cardUpvotes: List[CardUpvote]
        self.resolvableParticipants: List[ResolvableParticipant]
        self.userReportSettings: List[UserReportSetting]
        self.cardOrders: List[CardOrder]
        self.accountUserAchievements: List[AccountUserAchievement]
        self.userInviteCodes: List[UserInviteCode]
        self.decks: List[Deck]
        self.queueEntries: List[QueueEntry]
        self.anyDecks: List[Deck]
        self.projects: List[Project]
        self.archivedProjects: List[Project]
        self.anyProjects: List[Project]
        self.onboardingDeck: Deck
        self.deckSubscriptions: List[DeckSubscription]
        self.roles: List[AccountRole]
        self.invitations: List[UserInvitation]
        self.githubIntegration: Integration
        self.slackIntegration: Integration
        self.affiliateCodes: List[AffiliateCode]
        self.activities: List[Activity]
        self.stripeAccountSync: StripeAccountSync
        self.accountOnboarding: AccountOnboarding


class ActiveTimeTracker(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.card: Card
        self.createdAt: datetime.datetime
        self.user: User


class Activity(_BaseModel):
    def __init__(self, **kwargs):
        self.card: Card
        self.changer: User
        self.createdAt: datetime.datetime
        self.data: str
        self.deck: Deck
        self.isRemovedFromDeckEntry: bool
        self.isRemovedFromMilestoneEntry: bool
        self.milestone: Milestone
        self.project: Project
        self.type: str


class AffiliateCodeStat(_BaseModel):
    def __init__(self, **kwargs):
        self.affiliateCode: AffiliateCode
        self.month: int
        self.newVisitors: int
        self.revenue: int
        self.signups: int
        self.visits: int
        self.year: int


class AffiliateCode(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.code: str
        self.createdAt: datetime.datetime
        self.creator: User
        self.isDeleted: bool
        self.isDisabled: bool
        self.label: str
        self.message: str
        self.remainingRedemptions: int
        self.reward: str
        self.validUntil: Any
        self.vanityUrl: str
        self.stats: List[AffiliateCodeStat]


class AssigneeAssignment(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.assignedBy: User
        self.assignee: User
        self.lastAssignedAt: datetime.datetime


class AssigneeDeckAssignment(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.assignedBy: User
        self.assignee: User
        self.deck: Deck
        self.lastAssignedAt: datetime.datetime


class Attachment(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.card: Card
        self.content: str
        self.createdAt: datetime.datetime
        self.creator: User
        self.file: File
        self.title: str


class CardDiffNotification(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.asOwner: bool
        self.card: Card
        self.changers: list
        self.changes: str
        self.createdAt: datetime.datetime
        self.lastUpdatedAt: datetime.datetime
        self.user: User


class CardHistory(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.card: Card
        self.changer: User
        self.diff: str
        self.version: int
        self.versionCreatedAt: datetime.datetime


class CardOrderInDeck(_BaseModel):
    def __init__(self, **kwargs):
        self.card: Card
        self.changer: User
        self.deck: Deck
        self.sortIndex: str


class CardOrder(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.card: Card
        self.label: str
        self.sortValue: str


class CardPreset(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.createdAt: datetime.datetime
        self.creator: User
        self.data: str
        self.name: str


class CardSubscription(_BaseModel):
    def __init__(self, **kwargs):
        self.card: Card
        self.createdAt: datetime.datetime
        self.user: User


class CardUpvote(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.card: Card
        self.createdAt: datetime.datetime
        self.discordUserInfo: str
        self.type: str
        self.user: User


class Card(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.accountSeq: str
        self.assignee: User
        self.checkboxInfo: list
        self.checkboxStats: str
        self.content: str
        self.coverFile: File
        self.createdAt: datetime.datetime
        self.creator: User
        self.deck: Deck
        self.discordGuild: DiscordGuild
        self.dueDate: datetime.datetime
        self.effort: Any
        self.embeds: str
        self.hasBlockingDeps: bool
        self.isDoc: bool
        self.isPublic: bool
        self.lastUpdatedAt: datetime.datetime
        self.legacyProject: Project
        self.legacyProjectSeq: int
        self.masterTags: list
        self.mentionedUsers: list
        self.meta: str
        self.milestone: Milestone
        self.parentCard: Card
        self.priority: str
        self.sourceWorkflowItemId: WorkflowItem
        self.status: str
        self.tags: list
        self.title: str
        self.version: str
        self.visibility: str
        self.resolvables: List[Resolvable]
        self.handCards: List[HandCard]
        self.timeTrackingSegments: List[TimeTrackingSegment]
        self.cardSubscriptions: List[CardSubscription]
        self.resolvableEntries: List[ResolvableEntry]
        self.attachments: List[Attachment]
        self.diffs: List[CardHistory]
        self.totalTimeTrackingSums: TimeTrackingSum
        self.userTimeTrackingSums: List[TimeTrackingSum]
        self.childCards: List[Card]
        self.inDeps: List[Card]
        self.outDeps: List[Card]
        self.cardReferences: List[Card]
        self.upvotes: List[CardUpvote]


class CardsEffortHistory(_BaseModel):
    def __init__(self, **kwargs):
        self.cardCount: int
        self.date: datetime.datetime
        self.effortSum: int


class CardsFinishedHistory(_BaseModel):
    def __init__(self, **kwargs):
        self.assignee: User
        self.cardCount: int
        self.date: datetime.datetime
        self.effortSum: int


class CardsStatusHistory(_BaseModel):
    def __init__(self, **kwargs):
        self.count: int
        self.date: datetime.datetime
        self.status: str


class CardsTimeToFinished(_BaseModel):
    def __init__(self, **kwargs):
        self.assignee: User
        self.card: Card
        self.doneAt: datetime.datetime
        self.effort: int
        self.startedAt: datetime.datetime


class DailyDiscordGuildVoteMembership(_BaseModel):
    def __init__(self, **kwargs):
        self.discordGuild: DiscordGuild
        self.membershipCount: int
        self.t: datetime.datetime


class DailyPublicProjectMembership(_BaseModel):
    def __init__(self, **kwargs):
        self.membershipCount: int
        self.project: Project
        self.t: datetime.datetime


class PublicProjectVisit(_BaseModel):
    def __init__(self, **kwargs):
        self.project: Project
        self.t: datetime.datetime
        self.topReferrers: str
        self.visitCounts: int


class DeckAssignment(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.deck: Deck
        self.lastAssignedAt: datetime.datetime
        self.user: User


class DeckOrder(_BaseModel):
    def __init__(self, **kwargs):
        self.deck: Deck
        self.project: Project
        self.sortIndex: str
        self.user: User


class DeckPublicOrder(_BaseModel):
    def __init__(self, **kwargs):
        self.deck: Deck
        self.project: Project
        self.sortIndex: str


class DeckSubscription(_BaseModel):
    def __init__(self, **kwargs):
        self.deck: Deck
        self.user: User


class Deck(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.accountSeq: int
        self.content: str
        self.coverColor: str
        self.coverFile: File
        self.createdAt: datetime.datetime
        self.creator: User
        self.defaultCard: str
        self.defaultProjectTag: ProjectTag
        self.handSyncEnabled: bool
        self.isDeleted: bool
        self.isOnboardingDeck: bool
        self.manualOrderLabels: str
        self.milestone: Milestone
        self.preferredOrder: Any
        self.project: Project
        self.stats: str
        self.stickyDefaultProjectTag: bool
        self.title: str
        self.cards: List[Card]
        self.workflowItems: List[WorkflowItem]
        self.cardOrderInDecks: List[CardOrderInDeck]
        self.activities: List[Activity]


class DiscordGuild(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.createdAt: datetime.datetime
        self.discordGuildId: str
        self.guildIconId: str
        self.guildName: str
        self.karmaRoleThresholds: str
        self.removeCommandEmoji: str
        self.removeCommandEnabled: str
        self.removeCommandRoleId: str
        self.scope: str
        self.slashCommands: List[DiscordSlashCommand]
        self.projectNotifications: List[DiscordProjectNotification]
        self.dailyDiscordGuildVoteMemberships: List[DailyDiscordGuildVoteMembership]
        self.members: List[DiscordMember]


class DiscordMember(_BaseModel):
    def __init__(self, **kwargs):
        self.avatar: str
        self.createdAt: datetime.datetime
        self.deckyScore: int
        self.discordGuild: DiscordGuild
        self.discordUserId: str
        self.discriminator: str
        self.name: str
        self.nick: str


class DiscordProjectNotification(_BaseModel):
    def __init__(self, **kwargs):
        self.createdAt: datetime.datetime
        self.disabledTypes: str
        self.discordChannelId: str
        self.discordGuild: DiscordGuild
        self.project: Project


class DiscordSlashCommand(_BaseModel):
    def __init__(self, **kwargs):
        self.autoAddRoleToThread: str
        self.channelId: str
        self.deck: Deck
        self.description: str
        self.discordGuild: DiscordGuild
        self.karmaForCompletion: int
        self.leaderboard: str
        self.name: str
        self.permissions: str
        self.reaction: str
        self.reactionThreshold: int
        self.statusMessages: str
        self.statusTargetChannelId: str


class DueCard(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.card: Card
        self.createdAt: datetime.datetime
        self.user: User


class File(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.createdAt: datetime.datetime
        self.deletedAt: datetime.datetime
        self.deletedBy: User
        self.isDeleted: bool
        self.meta: str
        self.name: str
        self.selfHosted: bool
        self.size: str
        self.uploader: User
        self.url: str


class HandCard(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.card: Card
        self.sortIndex: int
        self.user: User


class Integration(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.createdAt: datetime.datetime
        self.creator: User
        self.disabled: str
        self.type: str
        self.user: User
        self.userData: str
        self.version: int


class Invoice(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.chargeData: str
        self.charged: int
        self.createdAt: datetime.datetime
        self.invoiceNumber: str
        self.subtotal: int
        self.total: int
        self.url: str


class LastSeenCardUpvote(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.createdAt: datetime.datetime
        self.lastSeenAt: datetime.datetime
        self.user: User


class MilestoneProgress(_BaseModel):
    def __init__(self, **kwargs):
        self.milestone: Milestone
        self.progress: str


class MilestoneProject(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.milestone: Milestone
        self.project: Project


class Milestone(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.accountSeq: int
        self.color: str
        self.createdAt: datetime.datetime
        self.creator: User
        self.date: datetime.datetime
        self.description: str
        self.handSyncEnabled: bool
        self.isDeleted: str
        self.isGlobal: bool
        self.manualOrderLabels: str
        self.name: str
        self.stats: str
        self.milestoneProjects: List[MilestoneProject]
        self.cards: List[Card]
        self.activities: List[Activity]
        self.progress: List[MilestoneProgress]


class ProjectOrder(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.project: Project
        self.sortIndex: str
        self.user: User


class ProjectSelection(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.project: Project
        self.user: User


class ProjectTag(_BaseModel):
    def __init__(self, **kwargs):
        self.color: str
        self.createdAt: datetime.datetime
        self.emoji: str
        self.project: Project
        self.tag: str


class ProjectUserSetting(_BaseModel):
    def __init__(self, **kwargs):
        self.project: Project
        self.receivePublicProjectDigest: bool
        self.user: User


class ProjectUser(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.project: Project
        self.projectRole: str
        self.user: User


class Project(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.accountSeq: int
        self.allowUpvotes: bool
        self.commentsArePublic: bool
        self.coverFile: File
        self.createdAt: datetime.datetime
        self.defaultUserAccess: str
        self.id: str
        self.isPublic: bool
        self.markerColor: Any
        self.name: str
        self.publicBackgroundColor: str
        self.publicBackgroundImage: File
        self.publicBannerFile: File
        self.publicHeading: str
        self.publicIsExplicit: bool
        self.publicLayoutVersion: int
        self.publicMessage: str
        self.publicPath: str
        self.publicRegistryAgreement: bool
        self.publicTileFile: File
        self.visibility: str
        self.decks: List[Deck]
        self.deckPublicOrders: List[DeckPublicOrder]
        self.milestoneProjects: List[MilestoneProject]
        self.publicProjectVisits: List[PublicProjectVisit]
        self.dailyPublicProjectMembership: List[DailyPublicProjectMembership]
        self.publicProjectMemberships: List[PublicProjectMembership]
        self.cardUpvotes: List[CardUpvote]
        self.cards: List[Card]
        self.tags: List[ProjectTag]
        self.activities: List[Activity]
        self.explicitProjectUsers: List[ProjectUser]
        self.access: List[UserProjectAccess]
        self.publicProjectInfo: PublicProjectInfo


class PublicProjectInfo(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.activities7d: str
        self.cardCount: str
        self.cardDoneStreak: str
        self.lastActivityAt: str
        self.project: Project
        self.visits7d: str


class PublicProjectMembership(_BaseModel):
    def __init__(self, **kwargs):
        self.createdAt: datetime.datetime
        self.digestFrequencyInDays: int
        self.project: Project
        self.user: User


class QueueEntry(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.card: Card
        self.cardDoneAt: datetime.datetime
        self.createdAt: datetime.datetime
        self.isCleared: bool
        self.sortIndex: int
        self.user: User


class QueueSelection(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.queueUser: User
        self.sortIndex: int
        self.user: User


class Release(_BaseModel):
    def __init__(self, **kwargs):
        self.content: str
        self.createdAt: datetime.datetime
        self.isLive: str
        self.title: str
        self.version: str


class ResolvableEntryHistory(_BaseModel):
    def __init__(self, **kwargs):
        self.author: User
        self.content: str
        self.lastChangedAt: datetime.datetime
        self.resolvable: Resolvable
        self.version: int


class ResolvableEntry(_BaseModel):
    def __init__(self, **kwargs):
        self.author: User
        self.content: str
        self.createdAt: datetime.datetime
        self.lastChangedAt: datetime.datetime
        self.meta: str
        self.resolvable: Resolvable
        self.version: str
        self.histories: List[ResolvableEntryHistory]


class ResolvableNotification(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.createdAt: datetime.datetime
        self.isLastParticipant: bool
        self.isParticipating: bool
        self.isSnoozing: bool
        self.lastUpdatedAt: datetime.datetime
        self.latestEntry: ResolvableEntry
        self.latestSeenEntry: ResolvableEntry
        self.resolvable: Resolvable
        self.snoozeUntil: datetime.datetime
        self.unseenAuthors: list
        self.unseenEntryCount: int
        self.user: User


class ResolvableParticipantHistory(_BaseModel):
    def __init__(self, **kwargs):
        self.addedBy: User
        self.done: bool
        self.firstJoinedAt: str
        self.lastChangedAt: datetime.datetime
        self.resolvable: Resolvable
        self.user: User
        self.version: int


class ResolvableParticipant(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.addedBy: User
        self.discordUserId: str
        self.done: bool
        self.firstJoinedAt: str
        self.lastChangedAt: str
        self.resolvable: Resolvable
        self.user: User


class Resolvable(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.card: Card
        self.closedAt: datetime.datetime
        self.closedBy: User
        self.context: str
        self.contextAsPrio: str
        self.createdAt: datetime.datetime
        self.creator: User
        self.isClosed: str
        self.isPublic: bool
        self.participants: List[ResolvableParticipant]
        self.participantHistories: List[ResolvableParticipantHistory]
        self.entries: List[ResolvableEntry]


class SavedSearch(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.forceOr: bool
        self.owner: User
        self.tokens: list


class StripeAccountSync(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.billingCycleEnd: datetime.datetime
        self.billingCycleStart: datetime.datetime
        self.centsPerSeat: int
        self.euVatIdData: str
        self.grossActualBalance: int
        self.grossBonusBalance: int
        self.hasBeenCancelledAt: datetime.datetime
        self.netGiftBalance: int
        self.paymentMethod: str
        self.pendingPlanType: str
        self.planName: str
        self.planType: str
        self.repeatingCoupon: str
        self.status: str
        self.vatCountryCode: str
        self.vatTaxPercentage: int


class TimeTrackingSegment(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.addedManually: bool
        self.card: Card
        self.createdAt: datetime.datetime
        self.finishedAt: datetime.datetime
        self.modifyDurationMsBy: int
        self.startedAt: datetime.datetime
        self.user: User


class TimeTrackingSum(_BaseModel):
    def __init__(self, **kwargs):
        self.card: Card
        self.runningModifyDurationMsBy: int
        self.runningStartedAt: datetime.datetime
        self.sumMs: int
        self.user: User


class UserDismissedHint(_BaseModel):
    def __init__(self, **kwargs):
        self.createdAt: datetime.datetime
        self.hintKey: str
        self.returnAt: datetime.datetime
        self.user: User


class UserEmail(_BaseModel):
    def __init__(self, **kwargs):
        self.createdAt: datetime.datetime
        self.email: str
        self.isPrimary: str
        self.isVerified: str
        self.user: User


class UserInvitation(_BaseModel):
    def __init__(self, **kwargs):
        self.accessToProjectIds: list
        self.account: Account
        self.createdAt: datetime.datetime
        self.email: str
        self.inviter: User
        self.role: str


class UserInviteCode(_BaseModel):
    def __init__(self, **kwargs):
        self.accessToProjectIds: list
        self.account: Account
        self.createdAt: datetime.datetime
        self.creator: User
        self.isActive: bool
        self.role: str
        self.token: str
        self.useCount: int
        self.validUntil: datetime.datetime


class UserOnboarding(_BaseModel):
    def __init__(self, **kwargs):
        self.steps: str
        self.user: User


class UserProjectAccess(_BaseModel):
    def __init__(self, **kwargs):
        self.project: Project
        self.projectRole: str
        self.role: str
        self.user: User


class UserTag(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.createdAt: datetime.datetime
        self.tag: str
        self.user: User


class User(_BaseModel):
    def __init__(self, **kwargs):
        self.autoMeFilterCardLimit: int
        self.cdxRole: str
        self.createdAt: datetime.datetime
        self.disableAnimations: bool
        self.disableMovingImages: bool
        self.disableSpellcheck: bool
        self.fullName: str
        self.hasPassword: str
        self.isIntegration: bool
        self.lastSeenRelease: Release
        self.name: str
        self.profileImage: File
        self.showCardIdInTimer: bool
        self.statusColorPalette: str
        self.timezone: str
        self.wantsConvoDigestMail: bool
        self.wantsDailyDigestMail: bool
        self.wantsNewsletter: bool
        self.deckOrders: List[DeckOrder]
        self.projectOrders: List[ProjectOrder]
        self.projectSelections: List[ProjectSelection]
        self.queueSelections: List[QueueSelection]
        self.accountRoles: List[AccountRole]
        self.cardDiffNotifications: List[CardDiffNotification]
        self.resolvableNotifications: List[ResolvableNotification]
        self.publicProjectMembership: List[PublicProjectMembership]
        self.lastSeenCardUpvotes: List[LastSeenCardUpvote]
        self.dueCards: List[DueCard]
        self.savedSearches: List[SavedSearch]
        self.activities: List[Activity]
        self.emails: List[UserEmail]
        self.tags: List[UserTag]
        self.unverifiedEmails: List[UserEmail]
        self.primaryEmail: UserEmail
        self.pinnedMilestone: Milestone
        self.explicitProjectAccess: List[ProjectUser]
        self.withProjectAccess: List[UserProjectAccess]
        self.projectSettings: List[ProjectUserSetting]
        self.accountSettings: List[AccountUserSetting]
        self.dismissedHints: List[UserDismissedHint]
        self.slackIntegrations: List[Integration]
        self.activeTimeTracker: ActiveTimeTracker
        self.participations: List[ResolvableParticipant]
        self.upvotes: List[CardUpvote]
        self.userOnboarding: UserOnboarding


class UserReportEmail(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.createdAt: datetime.datetime
        self.email: str
        self.enabled: str
        self.userReportSetting: UserReportSetting


class UserReportSetting(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.createdAt: datetime.datetime
        self.deckMapping: str
        self.fileSizeBytesLimit: int
        self.id: str
        self.name: str
        self.prioMapping: str
        self.reportTokens: List[UserReportToken]


class UserReportToken(_BaseModel):
    def __init__(self, **kwargs):
        self.createdAt: datetime.datetime
        self.enabled: str
        self.label: str
        self.reportCount: int
        self.userReportSetting: UserReportSetting


class Wizard(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.createdAt: datetime.datetime
        self.currentStep: str
        self.data: str
        self.finishedAt: datetime.datetime
        self.name: str


class WorkflowItemHistory(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.changer: User
        self.diff: str
        self.version: int
        self.versionCreatedAt: datetime.datetime


class WorkflowItem(_BaseModel):
    def __init__(self, **kwargs):
        self.account: Account
        self.accountSeq: str
        self.assignee: User
        self.checkboxInfo: list
        self.checkboxStats: str
        self.content: str
        self.createdAt: datetime.datetime
        self.creator: User
        self.deck: Deck
        self.effort: Any
        self.lastUpdatedAt: datetime.datetime
        self.masterTags: list
        self.mentionedUsers: list
        self.priority: str
        self.sortOrder: str
        self.tags: list
        self.targetDeck: Deck
        self.title: str
        self.version: str
        self.visibility: str
        self.diffs: List[WorkflowItemHistory]
        self.inDeps: List[WorkflowItem]
        self.outDeps: List[WorkflowItem]


# For convenience, create list of all the model classes:
model_classes = {
    model[0]: model[1]
    for model in inspect.getmembers(sys.modules[__name__], inspect.isclass)
    if model[1] != _BaseModel
}

# Create a single instance of the model cache for convenience:
model_cache = _ModelCache()
